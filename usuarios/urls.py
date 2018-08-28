from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='usuarios'),
    path('login/', views.login, name='login'),
	path('cadastrar/', views.cadastro, name='cadastrar'),  
	path('cadastrarusuario/', views.cadastrar_usuario, name='cadastrarusuario'), 
	path('logar/', views.logar, name='logar'), 
	path('sair/', views.sair, name='sair'), 
]