# **Project Documentation**

## **How to Run the Project**

### **Step 1: Set Up Virtual Environment**

1. **Download the Project Files**: After downloading the project files, open a terminal window in the project directory.

2. **Create a Virtual Environment**: Use the following command to create a virtual environment:
   ```bash
   python -m venv my_env
   ```

3. **Activate the Virtual Environment**: Once created, activate the virtual environment with the following command:
   ```bash
   my_env\Scripts\activate
   ```

4. **Install Required Packages**: Install all dependencies listed in `requirements.txt` by running:
   ```bash
    pip install -r requirements.txt
   ```
### **Step 2: Run The Project**

1. **Navigate to the Django Project Directory**: Ensure you're in the directory containing `manage.py`.

2. **Start the Django Server**:  Run the following command to start the server:
   ```bash
    python manage.py runserver
   ```
3. **Access the API Endpoint**:  Once the server is running, you can interact with the API using a tool like Postman. The API endpoint for predictions is:
    ```ruby
    http://127.0.0.1:8000/api/predict/
    ```
4. **Send a POST Request in Postman**: 
* Method: `POST`
* URL: `http://127.0.0.1:8000/api/predict/`
* Body: Select `raw` and choose `JSON` as the data format. Use the following JSON structure as a sample request:

  ```json
    {
    "0": {
        "num_clients": 20,
        "Sum of Instances in Clients": 17280,
        "Max. Of Instances in Clients": 864,
        "Min. Of Instances in Clients": 864,
        "Stddev of Instances in Clients": 0,
        "Average Dataset Missing Values %": 5.05787037,
        "Min Dataset Missing Values %": 3.356481481,
        "Max Dataset Missing Values %": 6.712962963,
        "Stddev Dataset Missing Values %": 1.020948805,
        "Average Target Missing Values %": 5.05787037,
        "Min Target Missing Values %": 3.356481481,
        "Max Target Missing Values %": 6.712962963,
        "Stddev Target Missing Values %": 1.020948805,
        "No. Of Features": 7,
        "No. Of Numerical Features": 7,
        "No. Of Categorical Features": 0,
        "Sampling Rate": 0.166666667,
        "Average Skewness of Numerical Features": 2.471131199,
        "Minimum Skewness of Numerical Features": 3.46E-06,
        "Maximum Skewness of Numerical Features": 5.030777624,
        "Stddev Skewness of Numerical Features": 0.678584581,
        "Average Kurtosis of Numerical Features": 10.94694511,
        "Minimum Kurtosis of Numerical Features": 0.009604812,
        "Maximum Kurtosis of Numerical Features": 31.80358209,
        "Stddev Kurtosis of Numerical Features": 4.069728429,
        "Avg No. of Symbols per Categorical Features": 0,
        "Min. No. Of Symbols per Categorical Features": 0,
        "Max. No. Of Symbols per Categorical Features": 0,
        "Stddev No. Of Symbols per Categorical Features": 0,
        "Avg No. Of Stationary Features": 5.8,
        "Min No. Of Stationary Features": 1,
        "Max No. Of Stationary Features": 7,
        "Stddev No. Of Stationary Features": 1.661324773,
        "Avg No. Of Stationary Features after 1st order": 6.05,
        "Min No. Of Stationary Features after 1st order": 6,
        "Max No. Of Stationary Features after 1st order": 7,
        "Stddev No. Of Stationary Features after 1st order": 0.217944947,
        "Avg No. Of Stationary Features after 2nd order": 7,
        "Min No. Of Stationary Features after 2nd order": 7,
        "Max No. Of Stationary Features after 2nd order": 7,
        "Stddev No. Of Stationary Features after 2nd order": 0,
        "Avg No. Of Significant Lags in Target": 6,
        "Min No. Of Significant Lags in Target": 6,
        "Max No. Of Significant Lags in Target": 6,
        "Stddev No. Of Significant Lags in Target": 0,
        "Avg No. Of Insignificant Lags in Target": 4,
        "Min No. Of Insignificant Lags in Target": 4,
        "Max No. Of Insignificant Lags in Target": 4,
        "Stddev No. Of Insignificant Lags in Target": 0,
        "Avg. No. Of Seasonality Components in Target": 0,
        "Max No. Of Seasonality Components in Target": 0,
        "Min No. Of Seasonality Components in Target": 0,
        "Stddev No. Of Seasonality Components in Target": 0,
        "Average Fractal Dimensionality Across Clients of Target": 0.062240441,
        "Maximum Period of Seasonality Components in Target Across Clients": 0,
        "Minimum Period of Seasonality Components in Target Across Clients": 0,
        "Entropy of Target Stationarity": 0.325082973
        }
    }
  ```

5. **Expected API Response: After sending the request, you should receive a response similar to this**
    ```json
    {
    "0": {
        "XGBRegressor": 0.64,
        "LinearSVR": 0.15,
        "HUBERREGRESSOR": 0.1,
        "LASSO": 0.08,
        "QUANTILEREGRESSOR": 0.02,
        "ELASTICNETCV": 0.0
        }
    }
    ```
    
7. **Deactivate Virtual Environment**: deactivate the virtual environment when you are done, like this in the terminal:
    ```bash
    deactivate
    ```

**Ensure you keep the virtual environment activated while running the project and installing any additional dependencies in the future.**

**Enjoy using the project!**

**Note: There are two models, you can use both and see how does this affect the results**