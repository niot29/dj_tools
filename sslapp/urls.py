from django import views
from django.urls import path
from .views import (
    SslCheckList,
    SslCheckCreateView,
    SslcheckDetele
)


urlpatterns = [
    path('check/', SslCheckList.as_view(), name='sslapp-sslcheck'),
    path('check/create/', SslCheckCreateView.as_view(), name='sslapp-check-create'),
    path('check/delete/<int:pk>', SslcheckDetele.as_view(), name='sslapp-check-delete'),
]