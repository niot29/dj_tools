from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Services(models.Model):
    service_title = models.CharField(max_length=100)
    service_desc = models.TextField()
    service_create_date = models.DateTimeField(default=timezone.now)
    service_author = models.ForeignKey(User,on_delete=models.CASCADE)
    service_status = models.IntegerField(default=1)
    
    def __str__(self):
        return self.service_title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})