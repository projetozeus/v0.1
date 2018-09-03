from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='reservas'),
    path('pacotes', views.pacotes, name='pacotes'),
    path('<int:pacote_id>/pacote/', views.pacote, name='pacote'),
    path('reserva', views.reserva, name='reserva'),
]
