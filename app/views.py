from django.shortcuts import render
from app.forms import Cadatro_LojasForm

# Create your views here.
def home(request):
    return render(request, 'index.html')


def form(request):
    data ={}
    data['form'] = Cadatro_LojasForm
    return render(request, 'form.html', data)

