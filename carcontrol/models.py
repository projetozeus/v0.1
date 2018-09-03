from django.db import models

class Condutores(models.Model):

	condutor_nome = models.CharField(max_length=200, default='null')

	def __str__(self):
		return self.condutor_nome

class Carro(models.Model):

	carro_modelo = models.CharField(max_length=200)

	def __str__(self):
		return self.carro_modelo

class Viagens(models.Model):

	viagens_kilometros = models.DecimalField(max_digits=5, decimal_places=2)
	viagens_carro = models.ForeignKey('Carro','on_delete.CASCADE')
	viagens_data = models.DateField()
	viagens_destino = models.CharField(max_length=200, default='null')
	viagens_condutor = models.ForeignKey('Condutores','on_delete.CASCADE',related_name='condutores')

	def __str__(self):
		return self.viagens_destino
