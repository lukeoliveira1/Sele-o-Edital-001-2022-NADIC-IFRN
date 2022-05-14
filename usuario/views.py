from django.shortcuts import render, redirect
from .forms import UsuarioForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import login, authenticate #add this

# Create your views here.

def register(request):
	if request.method == "POST":
		form = UsuarioForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("eleicao_urls:paginaInicial")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	
	form = UsuarioForm()	
	return render (request=request, template_name="cadastros/cadastrarUsuario.html", context={"register_form":form})


def my_login(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user) 
				return redirect("eleicao_urls:paginaInicial") # Indica para direcionar após fazer login
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login/login.html", context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Você realizou logout com sucesso!") 
	return redirect("eleicao_urls:paginaInicial")

def register_request(request):
	if request.method == "POST":
		form = UsuarioForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("eleicao_urls:paginaInicial")
		messages.error(request, "Unsuccessful registration. Invalid information.")	
	form = UsuarioForm()
	return render (request=request, template_name="cadastros/cadastrarUsuario.html", context={"register_form":form})