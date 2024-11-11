from django.urls import path
from . import views


urlpatterns = [
    path('', views.scanner_view, name='scanner'),
    path('submit-scan/', views.submit_scan, name='submit_scan'),
]