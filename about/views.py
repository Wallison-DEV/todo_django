from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_about(request):
    return HttpResponse('hello about')
