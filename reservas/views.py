from django.shortcuts import render

from .models import Pacote,Disponibildiade
from random import randint

import random

# Create your views here.

def index(request):

    context = {
		'x':'msg'
	}

    return render(request, 'reservas.html', context)


def pacotes(request):

    pacotes = Pacote.objects.all()

    context = {
		'x': pacotes
	}

    return render(request, 'pacotes/pacotes.html', context)


def pacote(request, pacote_id):

    pacote = Pacote.objects.filter(id=pacote_id)
    x = Disponibildiade.objects.values('disp_pacote__nome_pacote','uh_disponiveis__nome_uh').prefetch_related('pacote').filter(disp_pacote_id=pacote_id)

    for w in range(10):
        reg = str(random.randint(1,21)*132)

    context = {
		'x': x,
        'pacote':pacote,
        'reg':reg,
	}

    return render(request, 'pacotes/pacote.html', context)

def reserva(request):
        reg = 'PAR'

        context = {
    		'x': 'x',
    	}

        return render(request, 'pacotes/reserva.html', context)
