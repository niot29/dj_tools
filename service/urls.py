from django.urls import path
from .views import (
    ServicesListView
)
from service import views 

urlpatterns = [
    path('', ServicesListView.as_view(), name='service-home'),
    path('about/', views.about, name='sysset-about'),
]