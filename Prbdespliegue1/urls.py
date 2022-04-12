"""Prbdespliegue1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from usuario import views
from usuario.views import saludo

from xml.dom.minidom import Document
from django.urls import path

from django.conf import settings 
from django.conf.urls.static import static
from django.views.generic import TemplateView

# git https://github.com/wramdel/django_prb_1.git

#  git config --global user.email "wramdel@gmail.com"
#   git config --global user.name "Wilder Ramirez D"
# https://developer.mozilla.org/es/docs/Learn/Server-side/Django/Deployment
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', saludo),
]
