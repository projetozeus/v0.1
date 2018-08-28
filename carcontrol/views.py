from django.shortcuts import render
import operator
from . import views
from .models import Condutores, Viagens, Carro
from django.db.models import Count,Sum,Avg
from django.contrib.auth.decorators import login_required
from django_ajax.decorators import ajax
from django.db.models import Q
from django.views.generic import TemplateView
import json
from django.http import JsonResponse
from django.http import HttpResponse

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

	return render(request, 'carcontrol/principal.html', context)

@login_required
def condutores(request):

	x = Condutores.objects.values().aggregate()

	x = Condutores.objects.all()

	context = {
		'x':x
	}

	return render(request, 'carcontrol/condutores.html',context)

@login_required
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


	return render(request, 'carcontrol/viagens.html', context)

@login_required
def carros(request):

	x = Carro.objects.all()

	context = {
		'x':x
	}


	return render(request, 'carcontrol/carros.html', context)


def busca(request):

	if request.method == 'POST':

		vlr = request.POST.get("vlr", "")
		tbl = request.POST.get("tbl","")

		if tbl =="1":

			viagens = Viagens.objects.values('viagens_condutor',
			'viagens_carro_id',
			'viagens_data',
			'id',
			'viagens_destino',
			'viagens_kilometros',
			'viagens_carro__carro_modelo',
			'viagens_condutor__condutor_nome').prefetch_related('viagens_carro',
			'viagens_condutor').annotate(qtd=Count('viagens_condutor'),qtdCarro=Count('viagens_carro')).filter(viagens_destino = vlr)

			context = {
				'viagens':viagens
			}

		if vlr == "":

			viagens = Viagens.objects.values('viagens_condutor',
			'viagens_carro_id',
			'viagens_data',
			'id',
			'viagens_destino',
			'viagens_kilometros',
			'viagens_carro__carro_modelo',
			'viagens_condutor__condutor_nome').prefetch_related('viagens_carro',
			'viagens_condutor').annotate(qtd=Count('viagens_condutor'),qtdCarro=Count('viagens_carro'))

			context = {
				'viagens':viagens
			}

	return render(request,'carcontrol/busca.html', context)

#GRAFICO PAINEL DE CONTROLE PRINCIPAL / CARROS E CONDUTORES /

def chart(request):

	# INICIA ARRAYS VAZIAS PARA SEREM PREENCHIDAS COM OS VALORES A SEREM PASSADOS PELA REQUISICAO AJAX QUE FAZ O GRAFICO
	#da quantidade de viagens feitas por condutores

	nomes = []
	valores = []

	# QUERY QUE BUSCA OS DADOS DE VIAGENS FEITAS POR CONDUTOR

	viagens = Viagens.objects.values('viagens_condutor__condutor_nome').prefetch_related('viagens_carro',
			'viagens_condutor').annotate(qtd=Count('viagens_condutor'),qtdCarro=Count('viagens_carro'))

	tamanho = len(viagens)

	for x in range(0,tamanho):
		nomes.append(viagens[x]['viagens_condutor__condutor_nome'])
		valores.append(viagens[x]['qtd'])

	context = {
		'nomes': nomes,
		'valores': valores,
	}

	return JsonResponse(context)
