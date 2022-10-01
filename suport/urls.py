from django.urls import path
from suport.views import home, Contato, Sobre

urlpatterns = [
    path('', home ),
    path('contato/', Contato ),
    path('sobre/', Sobre ),
]
