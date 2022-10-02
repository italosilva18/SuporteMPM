from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'suporte/index.html', context={

        'nome': 'liz'
    })

def Painel(request):
    return render(request,'suporte/Painel.html')
def login(request):
    return render(request,'suporte/login.html')
