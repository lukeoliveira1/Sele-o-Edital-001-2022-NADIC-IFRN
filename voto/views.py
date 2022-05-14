from django.shortcuts import render
from .forms import votoForm

# Create your views here.
def cadastrarVoto(request):

    if request.method == 'GET':
        form = votoForm()
        context = {'primeiroForm' : form}
        print('--Entrou')
        return render(request, "cadastroVoto/formVoto.html", context)
    
    else:
        form = votoForm(request.POST) #pega o form preenchido

        if  form.is_valid(): # se tiver todo preenchido
            form.save()
            form = votoForm()

        context = {'primeiroForm' : form}
        return render(request, "cadastroVoto/formVoto.html", context)