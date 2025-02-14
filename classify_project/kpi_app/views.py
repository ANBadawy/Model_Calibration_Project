import os
import json
import joblib
import pandas as pd
import numpy as np  # Import NumPy
from sklearn.ensemble import RandomForestClassifier
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sklearn.preprocessing import StandardScaler

@csrf_exempt
def classify_instance(request):
    # Allow only POST requests
    if request.method != 'POST':
        return JsonResponse({'error': 'Only POST requests are allowed.'}, status=405)

    try:
        # Parse the request body
        request_body = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON provided. Ensure proper structure and format.'}, status=400)

    # Check if input is provided
    if not request_body:
        return JsonResponse({'error': 'Input data is required.'}, status=400)

    # Define the paths for model, scaler, and feature importance file
    model_path = os.path.join(
        settings.BASE_DIR,
        r'E:\Assignments\Calibration\Project_Calibration_Submission\Models\calibrated_model.pkl'
    )
    scaler_path = os.path.join(
        settings.BASE_DIR,
        r'E:\Assignments\Calibration\Project_Calibration_Submission\Models\scaler.pkl'
    )
    feature_importance_path = os.path.join(
        settings.BASE_DIR,
        r'E:\Assignments\Calibration\Project_Calibration_Submission\Models\all_57_feature_importance.csv'
    )

    # Load the classifier, scaler, and feature importance
    try:
        clf = joblib.load(model_path)
    except FileNotFoundError:
        return JsonResponse({'error': 'Model file not found. Please verify the model path.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Failed to load model: {str(e)}'}, status=500)

    try:
        scaler = joblib.load(scaler_path)
    except FileNotFoundError:
        return JsonResponse({'error': 'Scaler file not found. Please verify the scaler path.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Failed to load scaler: {str(e)}'}, status=500)

    try:
        feature_importances = pd.read_csv(feature_importance_path)
        # Check column names
        if 'feature' not in feature_importances.columns or 'importance' not in feature_importances.columns:
            return JsonResponse({'error': 'Feature importance file does not have the required columns: "feature" and "importance".'}, status=500)

        # Select important features based on the threshold
        important_features = feature_importances[
            feature_importances['importance'] >= 0.01
        ]['feature'].tolist()
    except FileNotFoundError:
        return JsonResponse({'error': 'Feature importance file not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': f'Failed to load feature importance: {str(e)}'}, status=500)

    try:
        label_encoder_path = os.path.join(
            settings.BASE_DIR,
            r'E:\Assignments\Calibration\Project_Calibration_Submission\Models\label_encoder.pkl'
        )
        label_encoder = joblib.load(label_encoder_path)
    except FileNotFoundError:
        raise Exception("Label encoder file not found. Please verify the path.")
    except Exception as e:
        raise Exception(f"Failed to load label encoder: {str(e)}")

    
    def predict_best_algorithms(meta_features_dict):
        output = {}
        for key, meta_features in meta_features_dict.items():
            try:
                # Convert the key to a standard Python type if it's not JSON-serializable
                key = int(key) if isinstance(key, (np.integer, np.int64)) else key

                # Convert meta_features to a DataFrame
                meta_features_df = pd.DataFrame([meta_features])

                # Ensure all required features are present
                missing_cols = set(important_features) - set(meta_features_df.columns)
                for col in missing_cols:
                    if len(meta_features_dict) > 1:
                        # Calculate mean for multiple inputs
                        mean_value = pd.DataFrame(meta_features_dict).transpose()[col].mean()
                        meta_features_df[col] = mean_value
                    else:
                        # Assign zero for a single input
                        meta_features_df[col] = 0

                # Reorder columns to match the training data
                meta_features_df = meta_features_df[important_features]

                # Scale features
                meta_features_scaled = scaler.transform(meta_features_df)

                # Predict probabilities
                prob = clf.predict_proba(meta_features_scaled)[0]

                # Map class labels to algorithm names using the label encoder
                class_names = label_encoder.inverse_transform(clf.classes_)
                prob_dict = {name: round(float(v), 2) for name, v in zip(class_names, prob)}
                
                # Sort by probabilities
                sorted_prob_dict = dict(sorted(prob_dict.items(), key=lambda item: item[1], reverse=True))

                output[key] = sorted_prob_dict
            except Exception as e:
                output[str(key)] = {'error': f'Failed to process input: {str(e)}'}
        return output

    
    try:
        # Get predictions
        predictions = predict_best_algorithms(request_body)
        return JsonResponse(predictions, status=200)

    except Exception as e:
        return JsonResponse({'error': f'Error processing input: {str(e)}'}, status=500)




