from django.urls import path

from . import views

urlpatterns = [
    path('', views.cc_index, name='carcontrol'),
    path('condutores/', views.condutores, name='condutores'),
    path('viagens/', views.viagens, name='viagens'),
    path('carros/', views.carros, name='carros'),
    path('busca/', views.busca, name='busca'),
    path('chart/', views.chart, name='chart'),
]
