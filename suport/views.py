from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def Home(request):
    return HttpResponse('Teste do home1')
def Contato(request):
    return HttpResponse('besta')
def Sobre(request):
    return HttpResponse('besta')