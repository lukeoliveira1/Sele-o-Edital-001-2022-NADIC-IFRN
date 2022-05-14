from django.urls import path
from .views import *

app_name = 'eleicao_urls'

urlpatterns = [
    path('', paginaInicial, name="paginaInicial"),
    path('cadastrarEleicao/', cadastrarEleicao, name='cadastrarEleicao'),
    path('editarEleicao/<int:id_eleicao>/',editarEleicao,name='editarEleicao'),
    path('detalheEleicao/<int:id_produto>/', detalheEleicao, name="detalheEleicao"), 
    path('resultados/', resultados, name="resultados"), 
]
