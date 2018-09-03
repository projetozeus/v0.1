from django.contrib import admin

from .models import Viagens, Carro, Condutores

admin.site.register(Viagens)
admin.site.register(Condutores)
admin.site.register(Carro)
