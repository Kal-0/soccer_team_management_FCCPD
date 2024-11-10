from django import forms
from .models import Jogador, Campeonato, Clube, Treinador, Medico

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
    # Verifique se o campo `clube` realmente existe no modelo `Jogador`
    clube = forms.ModelChoiceField(
        queryset=Clube.objects.all(), required=True, label="Clube")

    class Meta:
        model = Jogador
        fields = ['nome', 'cpf', 'posicao', 'numero', 'tempo_contrato',
                  'titular', 'dt_nascimento', 'salario', 'clube']

class TreinadorForm(forms.ModelForm):
    class Meta:
        model = Treinador
        fields = ['cpf', 'nome', 'categoria', 'tempo_contrato', 'cargo',
                   'dt_nascimento', 'salario', 'clube']

class MedicoForm(forms.ModelForm):
    clube = forms.ModelChoiceField(
        queryset=Clube.objects.all(), required=True, label="Clube")
    
    class Meta:
        model = Medico
        fields = ['nome', 'crm', 'especializacao', 'dt_nascimento', 'salario', 'clube']