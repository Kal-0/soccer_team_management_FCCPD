from django.db import models

class Campeonato(models.Model):
    nome = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    premiacao = models.CharField(max_length=100)
    dt_inicio = models.DateField()
    dt_termino = models.DateField()
    id = models.AutoField(primary_key=True) 

    def __str__(self):
        return self.nome

class Jogador(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=100, primary_key=True)
    posicao = models.CharField(max_length=50)
    numero = models.IntegerField()
    tempo_contrato = models.CharField(max_length=100)
    titular = models.BooleanField()
    dt_nascimento = models.DateField()
    salario = models.FloatField()

    def __str__(self):
        return self.nome
