from django.conf.urls import url
from django.urls import path

from . import view



urlpatterns = [
    url(r'^hello$', view.hello),
    url('m', view.m),
    path('add/<int:a>/<int:b>/', view.add2, name='add2'),
    url(r'^$', view.index),
    url(r'^asd',view.asd),
    path('myadd/', view.myadd, name='myadd'),  # new
]