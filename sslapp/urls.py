from . import views
from django.urls import path
from .views import (
    SslCheckList,
    SslCheckCreateView,
    SslcheckDetele,
    SslcheckDetail,
    SslCheckExec
    
)


urlpatterns = [
    path('check/', SslCheckList.as_view(), name='sslapp-sslcheck'),
    path('check/create/', SslCheckCreateView.as_view(), name='sslapp-check-create'),
    path('check/execheck/', views.SslCheckExec, name='sslapp-exec-check'),
    path('check/detail/<int:pk>', SslcheckDetail.as_view(), name='sslapp-check-detail'),
    path('check/delete/<int:pk>', SslcheckDetele.as_view(), name='sslapp-check-delete'),
]