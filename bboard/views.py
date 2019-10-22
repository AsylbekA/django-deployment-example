from django.shortcuts import render
from django.http import HttpResponse as hr

def index(request):
    return hr("Здесь будет выведен список обьявлений.")
# Create your views here.
