from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'recipes/home.html', context={

        'name': 'Alisson Miranda & Zeane Campos',
    }, status=404)

def contato(request):
    return HttpResponse('contato 1')

def sobre(request):
    return HttpResponse('sobre 1')