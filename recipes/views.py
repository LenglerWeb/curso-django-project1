from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Página HOME em views")

def sobre(request):
    return HttpResponse("Página SOBRE em views")

def contato(request):
    return HttpResponse("Página CONTATO em views")