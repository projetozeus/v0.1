from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

from django.contrib.auth import authenticate, login as dj_login, logout
from django.http import HttpResponseRedirect
# Create your views here.
from django.contrib.auth.decorators import login_required

def index(request):

	return render(request, 'usuarios/index.html')

# VIEW DO LOGIN

def login(request):


	return render(request,'usuarios/login.html')


#LOGAR 

def logar(request):

	next = request.POST['next']

	usuario_aux = User.objects.get(email=request.POST['email'])
	
	usuario = authenticate(username=usuario_aux.username,
						   password=request.POST['password'])
	if usuario is not None:
		dj_login(request, usuario)
		if next == '':

			return HttpResponseRedirect('/carcontrol/viagens')
		else:
			return HttpResponseRedirect(next,'')		
	else:
		return HttpResponseRedirect('/login/')

# VIEW DO CADASTRO

def cadastro(request):
	
	return render(request,'usuarios/cadastrar.html')


# CADASTRAR USUARIO

@require_POST

def cadastrar_usuario(request):

	# VVERIFICA SE USUARIO COM EMAIL JA CADASTRADO
	try:
		usuario_aux = User.objects.get(email=request.POST['email'])

		if usuario_aux:
			return render(request, 'usuarios/cadastrar.html', {'msg':'Erro. email ja cadastrado'})

	#CRIA USUARIO		
	except User.DoesNotExist:

		nome_usuario = request.POST['username']
		email = request.POST['email']
		senha = request.POST['password']
		novoUsuario = User.objects.create_user(username=nome_usuario, email=email, password=senha)
		novoUsuario.save()

	return render(request,'usuarios/login.html')


@login_required
def sair(request):
    logout(request)
    return HttpResponseRedirect('/usuarios/login/')