from django.shortcuts import render
from django.http import HttpResponse


def sslCheck(requst):
   return render(requst,'sslapp/ssl_check.html',{'title': 'About'})
