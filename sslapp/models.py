from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class sslSiteModel(models.Model):
    ssl_title = models.CharField(max_length=100)
    ssl_site = models.URLField()
    ssl_desc = models.TextField()
    ssl_cert_info = models.TextField()
    ssl_create_date = models.DateField(null=True, blank=True)
    ssl_expiry_date = models.DateField(null=True, blank=True)        
    ssl_last_check = models.DateField(null=True, blank=True)
    ssl_author = models.ForeignKey(User,on_delete=models.CASCADE)
    ssl_status = models.IntegerField(default=1)
    
    def __str__(self):
        return self.ssl_title