from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import sslSiteModel


## fin SslChckList work can delete
def sslCheck(requst):
   urlObject = requst.get_host()
   print({urlObject})
   return render(requst,'sslapp/ssl_check.html',{'title': 'About'})

class SslCheckList(ListView):
   model = sslSiteModel
   template_name = 'sslapp/ssl_check.html'
   context_object_name = 'sslcheckList'