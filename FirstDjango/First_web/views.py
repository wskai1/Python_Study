#coding=UTF-8
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from First_web import models
from First_web.models import Tab1


def index(request):
    return render(request, 'index.html')


def chaxun(request):
    tab = Tab1.objects.all()
    context = {
        'ArtiInfo': tab
    }
    return render(request, 'chaxun.html',context)

def delete(request):
    p1 = request.GET.get('id')
    Tab1.objects.filter(id=p1).delete()
    return HttpResponseRedirect("chaxun")

def add(request):
    p1 = request.GET.get('name')
    p2 = request.GET.get('sex')
    p3 = request.GET.get('age')
    print(p1),print(p2),print(p3)
    obj = models.Tab1(name=p1, sex=p2,age=p3)
    obj.save()
    return HttpResponseRedirect("chaxun")

