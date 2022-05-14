from django.shortcuts import get_object_or_404, redirect, render
from .forms import eleicaoForm
from .models import election
from django.contrib.auth.decorators import login_required

# Create your views here.
def paginaInicial(request):
    produtos = election.objects.all()
    return render(request, "paginaInicial.html", context={'produtos': produtos})

def resultados(request):
    return render(request, "resultados.html")

def detalheEleicao(request, id_produto):
    print("A eleição que você selecionou:", id_produto)
    produtos = election.objects.get(id=id_produto)
    return render(request, "main\detalheEleicao.html", context={'produto': produtos})

@login_required
def cadastrarEleicao(request):

    if request.method == 'GET':
        form = eleicaoForm()
        context = {'primeiroForm' : form}
        print('--Entrou')
        return render(request, "cadastroEleicao/formEleicao.html", context)
    
    else:
        form = eleicaoForm(request.POST) #pega o form preenchido

        if  form.is_valid(): # se tiver todo preenchido
            form.save()
            form = eleicaoForm()

        context = {'primeiroForm' : form}
        return render(request, "cadastroEleicao/formEleicao.html", context)

@login_required
def editarEleicao (request,id_eleicao):
    Eleicao = get_object_or_404(election, pk=id_eleicao) # traz a vaga pelo id passado.
    
    if request.method == 'POST':
        form = eleicaoForm(request.POST,instance=Eleicao)
        if form.is_valid():
            form.save()
            return redirect('eleicao_urls:paginaInicial')
    else:
        form = eleicaoForm(instance=Eleicao)   

## criando e preenchendo o formulário
    return render(request,'cadastroEleicao/formEleicao.html', context={"primeiroForm": form })