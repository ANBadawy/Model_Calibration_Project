from django.urls import path
from .views import classify_instance

urlpatterns = [
    path('predict/', classify_instance, name='classify_instance'),
]
