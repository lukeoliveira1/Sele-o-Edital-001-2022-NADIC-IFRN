from django.urls import path
from .views import *

app_name = 'votos_urls'

urlpatterns = [
    path('cadastrarVoto/', cadastrarVoto, name='cadastrarVoto'),
]
