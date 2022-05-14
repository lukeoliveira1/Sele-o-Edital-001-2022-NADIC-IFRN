from django.urls import path
from .views import *

app_name = 'candidato_urls'

urlpatterns = [
    path('cadastrarCandidato/', cadastrarCandidato, name='cadastrarCandidato'),
]
