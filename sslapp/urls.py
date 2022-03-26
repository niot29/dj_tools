from django import views
from django.urls import path
from .views import (
    SslCheckList,
    SslCheckCreateView
)


urlpatterns = [
    path('check/', SslCheckList.as_view(), name='sslapp-sslcheck'),
    path('create/', SslCheckCreateView.as_view(), name='sslapp-create-check'),
]