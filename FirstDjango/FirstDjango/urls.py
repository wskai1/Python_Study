#coding=UTF-8
"""FirstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url

import First_web
from First_web.views import index, chaxun, delete  # 导入views.py文件中的index函数

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^$', index), #在url中凡是以url开头的访问都使用index函数来处理该请求
    url('chaxun',chaxun),
    url('delete',  First_web.views.delete, name='delete'), #mysql删除
    url('add', First_web.views.add, name='add'),  # mysql删除
    url('add', First_web.views.add, name='add')  # mysql删除
]
