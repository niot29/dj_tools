from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Services

def home(request):
    return render(request,'service/index.html')

class ServicesListView(ListView):
    model = Services
    template_name = 'service/services.html'
    context_object_name = 'services'
    #ordering = ['-service_create_date']


def about(request):
    return render(request,'service/about.html')