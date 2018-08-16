from django.shortcuts import render
from . import views
from .models import Condutores, Viagens, Carro
from django.db.models import Count,Sum,Avg
from django.contrib.auth.decorators import login_required 

@login_required
def cc_index(request):
	
	x = Viagens.objects.values('viagens_condutor',
		'viagens_carro_id',
		'viagens_data',
		'id',
		'viagens_destino',
		'viagens_kilometros',
		'viagens_carro__carro_modelo',
		'viagens_condutor__condutor_nome').prefetch_related('viagens_carro',
		'viagens_condutor').annotate(qtd=Count('viagens_condutor'),qtdCarro=Count('viagens_carro')) 

	y = Viagens.objects.aggregate(soma=Sum('viagens_kilometros'),media=Avg('viagens_kilometros'))

	context = {	
		'x':x,
		'y':y
	}

	return render(request, 'principal.html', context)

def condutores(request):

	x = Condutores.objects.values().aggregate()

	x = Viagens.objects.values('viagens_condutor',
		'viagens_carro_id',
		'viagens_data',
		'id',
		'viagens_destino',
		'viagens_kilometros',
		'viagens_carro__carro_modelo',
		'viagens_condutor__condutor_nome').prefetch_related('viagens_carro',
		'viagens_condutor').annotate(qtd=Count('viagens_condutor'),qtdCarro=Count('viagens_carro')) 

	context = {
		'x':x
	}
	
	return render(request, 'condutores.html',context)

def viagens(request):

	x = Viagens.objects.values('viagens_condutor',
		'viagens_carro_id',
		'viagens_data',
		'id',
		'viagens_destino',
		'viagens_kilometros',
		'viagens_carro__carro_modelo',
		'viagens_condutor__condutor_nome').prefetch_related('viagens_carro',
		'viagens_condutor')

	context = {
		'x':x
	}
	

	return render(request, 'viagens.html', context)

def carros(request):

	x = Viagens.objects.values('viagens_condutor',
		'viagens_carro_id',
		'viagens_data',
		'id',
		'viagens_destino',
		'viagens_kilometros',
		'viagens_carro__carro_modelo',
		'viagens_condutor__condutor_nome').prefetch_related('viagens_carro',
		'viagens_condutor').annotate(qtd=Count('viagens_condutor'),qtdCarro=Count('viagens_carro')) 

	context = {
		'x':x
	}
	

	return render(request, 'carros.html', context)