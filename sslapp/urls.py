from django.urls import path
from .views import (
    SslCheckList
)


urlpatterns = [
    path('check/', SslCheckList.as_view(), name='sslapp-sslcheck'),
]