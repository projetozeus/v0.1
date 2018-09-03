from django.contrib import admin

from .models import CPF_Cliente, Pacote, Uh, Reserva, Disponibildiade

admin.site.register(CPF_Cliente)
admin.site.register(Pacote)
admin.site.register(Uh)
admin.site.register(Reserva)
admin.site.register(Disponibildiade)
