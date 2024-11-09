from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets  # type: ignore
from .forms import JogadorForm
from .models import Campeonato, Jogador
from .serializers import CampeonatoSerializer


class CampeonatoViewSet(viewsets.ModelViewSet):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer

# ==========================JOGADOR=======================================


def jogador_list(request):
    jogadores = Jogador.objects.all()
    return render(request, 'jogadores/listaJogador.html', {'jogadores': jogadores})


def jogador_create(request):
    if request.method == 'POST':
        form = JogadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jogadores/listaJogador')
    else:
        form = JogadorForm()
    return render(request, 'jogadores/formJogador.html', {'form': form})


def jogador_update(request, cpf):
    jogador = get_object_or_404(Jogador, cpf=cpf)
    if request.method == 'POST':
        form = JogadorForm(request.POST, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('jogadores/listaJogador')
    else:
        form = JogadorForm(instance=jogador)
    return render(request, 'jogadores/formJogador.html', {'form': form})


def jogador_delete(request, cpf):
    jogador = get_object_or_404(Jogador, cpf=cpf)
    if request.method == 'POST':
        jogador.delete()
        return redirect('jogadores/listaJogador')
    return render(request, 'jogadores/deleteJogador.html', {'jogador': jogador})
