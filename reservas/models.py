from django.db import models

# Create your models here.

class CPF_Cliente(models.Model):

    nome_cliente = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300)
    complemento = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.nome_cliente)

class Pacote(models.Model):
    nome_pacote = models.CharField(max_length=200)
    desc_pacote = models.CharField(max_length=400)
    valor_pacote = models.DecimalField(max_digits=5, decimal_places=2)
    data_pacote_entrada = models.DateField()
    data_pacote_saida = models.DateField()

    def __str__(self):
        return self.nome_pacote

class Uh(models.Model):
    nome_uh = models.CharField(max_length=100)
    valor_uh = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome_uh

class Reserva(models.Model):
    data_entrada = models.DateField()
    data_saida = models.DateField()
    situacao = models.BooleanField(default=False)
    reserva_cliente = models.ForeignKey('CPF_Cliente','on_delete.CASCADE',related_name='cpf_cliente')
    reserva_pacote = models.ForeignKey('Pacote','on_delete.CASCADE',related_name='pacote')
    reserva_uh = models.ForeignKey('Uh','on_delete.CASCADE',related_name='uh')
    cod_reserva = models.CharField(max_length=100)

    def __str__(self):
        return str(self.reserva_cliente)

class Disponibildiade(models.Model):
    disp_pacote =  models.ForeignKey('Pacote','on_delete.CASCADE',related_name='disp_pacote')
    uh_disponiveis = models.ManyToManyField(Uh)
