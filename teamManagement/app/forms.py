from django import forms
from .models import Jogador, Campeonato, Clube


class CampeonatoForm(forms.ModelForm):
    class Meta:
        model = Campeonato
        fields = ['nome', 'modelo', 'premiacao', 'dt_inicio', 'dt_termino']


class ClubeForm(forms.ModelForm):
    class Meta:
        model = Clube
        fields = ['nome', 'dt_fundacao', 'titulos']


class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'cpf', 'posicao', 'numero',
                  'tempo_contrato', 'titular', 'dt_nascimento', 'salario']
