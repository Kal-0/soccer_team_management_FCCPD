from django.shortcuts import render, redirect, get_object_or_404
from .forms import JogadorForm, CampeonatoForm
from .models import Campeonato, Jogador

# ==========================CAMPEONATO=======================================


def campeonato_list(request):
    campeonatos = Campeonato.objects.all()
    return render(request, 'campeonatos/listaCampeonato.html', {'campeonatos': campeonatos})


def campeonato_create(request):
    if request.method == 'POST':
        form = CampeonatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campeonatos/campeonato_list')
    else:
        form = CampeonatoForm()
    return render(request, 'campeonatos/formCampeonato.html', {'form': form})


def campeonato_update(request, id):
    campeonato = get_object_or_404(Campeonato, id=id)
    if request.method == 'POST':
        form = CampeonatoForm(request.POST, instance=campeonato)
        if form.is_valid():
            form.save()
            return redirect('campeonatos/campeonato_list')
    else:
        form = CampeonatoForm(instance=campeonato)
    return render(request, 'campeonatos/formCampeonato.html', {'form': form})


def campeonato_delete(request, id):
    campeonato = get_object_or_404(Campeonato, id=id)
    if request.method == 'POST':
        campeonato.delete()
        return redirect('campeonatos/campeonato_list')
    return render(request, 'campeonatos/deleteCampeonato.html', {'campeonato': campeonato})

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
