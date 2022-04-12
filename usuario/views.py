from pipes import Template
from django.shortcuts import render, HttpResponse
from django.template import Template, Context
from pyexpat import model
from re import template
from django.urls import path

# Create your views here.


def saludo(request):
    return HttpResponse("Hola Mundo")
