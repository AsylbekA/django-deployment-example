from django.urls import re_path, path
from .views import index, by_rubric, BbCreateView, add, add_save, add_and_save


urlpatterns = [
    path('add/', add_and_save, name='add'),
    path('add/save/', add_save, name='add'),
    path('add/', add, name='add'),
    re_path(r'^add/$', BbCreateView.as_view(), name='add'),
    re_path(r'^$', index, name='index'),
    re_path(r'^(?P<rubric_id>[0-9]*)/$', by_rubric, name='by_rubric'),
]