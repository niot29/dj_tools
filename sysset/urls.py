from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='sysset-home'),
    path('about/', views.about, name='sysset-about'),
]