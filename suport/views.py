from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'index.html')
def Contato(request):
    return HttpResponse('besta')
def Sobre(request):
    return HttpResponse('besta')