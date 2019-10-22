from django.http import HttpResponse
from .models import Bb


def index(request):
    bbs = Bb.objects.order_by('-published')
    return HttpResponse(request, 'bboard/index.html', {'bbs': bbs})
