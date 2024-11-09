from django import forms
from .models import Jogador, Campeonato, Clube


class CampeonatoForm(forms.ModelForm):
    class Meta:
        model = Campeonato
        fields = ['nome', 'modelo', 'premiacao', 'dt_inicio', 'dt_termino']


class ClubeForm(forms.ModelForm):
    campeonatos = forms.ModelMultipleChoiceField(
        queryset=Campeonato.objects.all(), required=False, label="Campeonatos")

    class Meta:
        model = Clube
        fields = ['nome', 'dt_fundacao', 'titulos', 'campeonatos']


class JogadorForm(forms.ModelForm):
    clube = forms.ModelChoiceField(
        queryset=Clube.objects.all(), required=True, label="Clube")

    class Meta:
        model = Jogador
        fields = ['nome', 'cpf', 'posicao', 'numero', 'tempo_contrato',
                  'titular', 'dt_nascimento', 'salario', 'clube']
