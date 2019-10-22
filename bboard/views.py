from django.shortcuts import render
from django.http import HttpResponse
from .models import Bb


def index(request):
    s = 'Список обьявлений \r\n\r\n\r\n'
    for bb in Bb.objects.order_by('-published'):
        s += bb.title + '\r\n' + bb.content + '\r\r\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8 ')
