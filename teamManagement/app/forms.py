from django import forms
from .models import Jogador, Campeonato

class CampeonatoForm(forms.ModelForm):
    class Meta:
        model = Campeonato
        fields = ['nome', 'modelo', 'premiacao', 'dt_inicio', 'dt_termino']

class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'cpf', 'posicao', 'numero', 'tempo_contrato', 'titular', 'dt_nascimento', 'salario']
