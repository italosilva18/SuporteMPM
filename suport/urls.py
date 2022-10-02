from django.urls import path
from suport.views import home, Painel, login

urlpatterns = [
    path('', home ),
    path('Painel', Painel ),
    path('login/', login ),
]
