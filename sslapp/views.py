from dataclasses import field, fields
from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
   ListView,
   DetailView,
   CreateView,
   DeleteView
)
from django.urls import reverse_lazy
from .models import sslSiteModel
from .forms import SslCheckModelForm
from bootstrap_modal_forms.generic import BSModalCreateView



## fin SslChckList work can delete
def sslCheck(requst):
   urlObject = requst.get_host()
   print({urlObject})
   return render(requst,'sslapp/ssl_check.html',{'title': 'About'})

class SslCheckList(ListView):
   model = sslSiteModel
   template_name = 'sslapp/ssl_check.html'
   context_object_name = 'sslcheckList'
   
class SslCheckCreateView(BSModalCreateView):
    template_name = 'sslapp/ssl_createcheck.html'
    form_class = SslCheckModelForm
    success_message = 'Success: Check URL was created.'
    success_url = reverse_lazy('sslapp-sslcheck')
   
class SslcheckDetele(DeleteView):
   pass
