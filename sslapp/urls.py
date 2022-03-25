from django.urls import path
from . import views

urlpatterns = [
    path('check/', views.sslCheck, name='sslapp-sslcheck'),
]