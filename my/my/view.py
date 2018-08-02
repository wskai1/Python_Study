# -*- coding: utf-8 -*-

# from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, render_to_response


def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)
def m(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'm.html', context)

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def index(request):
    context = {}
    context['condition1'] ='true',
    context['condition2'] = 'true',
    context['athlete_list'] = [1, 2, 3, 4, 5, 6, 7]
    return render(request, 'home.html',context)



def asd(request):
    context = {}
    from mydjango.models import tab1
    people_list = tab1.objects.all()
    context['people_list'] =people_list
    return render_to_response("showuser.html", context)

def myadd(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))