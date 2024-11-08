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
