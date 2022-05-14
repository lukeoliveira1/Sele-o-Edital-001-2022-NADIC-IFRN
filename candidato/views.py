from django.shortcuts import render
from .forms import candidatoForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def cadastrarCandidato(request):

    if request.method == 'GET':
        form = candidatoForm()
        context = {'primeiroForm' : form}
        print('--Entrou')
        return render(request, "cadastroCandidato/formCandidato.html", context)
    
    else:
        form = candidatoForm(request.POST) #pega o form preenchido

        if  form.is_valid(): # se tiver todo preenchido
            form.save()
            form = candidatoForm()

        context = {'primeiroForm' : form}
        return render(request, "cadastroCandidato/formCandidato.html", context)

