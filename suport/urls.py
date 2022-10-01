from django.urls import path
from suport.views import Home, Contato, Sobre

urlpatterns = [
    path('', Home ),
    path('contato/', Contato ),
    path('sobre/', Sobre ),
]
