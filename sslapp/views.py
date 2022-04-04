from dataclasses import field, fields
from pyexpat import model
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import (
   ListView,
   DetailView,
   CreateView,
   DeleteView
)
from django.urls import reverse_lazy
from . func_check import run_sslcheckModule
from .models import sslSiteModel
from .forms import SslCheckModelForm
from bootstrap_modal_forms.generic import BSModalCreateView,BSModalDeleteView,BSModalReadView



## fin SslChckList work can delete
def sslCheck(requst):
   urlObject = requst.get_host()
   print({urlObject})
   return render(requst,'sslapp/ssl_check.html',{'title': 'About'})

def SslCheckExec(request):
   run_sslcheckModule('google.com')
   print ("SslCheckExec -- ")
   return redirect('sslapp-sslcheck')

class SslCheckList(ListView):
   model = sslSiteModel
   template_name = 'sslapp/ssl_check.html'
   context_object_name = 'sslcheckList'
    
class SslCheckCreateView(BSModalCreateView):
    template_name = 'sslapp/ssl_createcheck.html'
    form_class = SslCheckModelForm
    success_message = 'Success: Check URL was created.'
    success_url = reverse_lazy('sslapp-sslcheck')

class SslcheckDetail(BSModalReadView):
    model = SslCheckModelForm
    template_name = 'sslapp/ssl_detail_check.html'
   
class SslcheckDetele(BSModalDeleteView):
   model = sslSiteModel
   template_name = 'sslapp/ssl_delete_check.html'
   success_message = 'Success: Check URL was created.'
   success_url = reverse_lazy('sslapp-sslcheck')

