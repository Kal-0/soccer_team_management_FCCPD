from django.shortcuts import render, redirect, get_object_or_404
from .forms import CampeonatoForm, ClubeForm, JogadorForm, TreinadorForm
from .models import Campeonato, Clube, Jogador, Treinador

# ========================== CAMPEONATO =======================================

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

# ========================== CLUBE =======================================

def clube_list(request):
    clubes = Clube.objects.all()
    return render(request, 'clubes/listaClube.html', {'clubes': clubes})


def clube_create(request):
    if request.method == 'POST':
        form = ClubeForm(request.POST)
        if form.is_valid():
            clube = form.save()  # Salva o clube para obter o ID
            campeonatos = form.cleaned_data['campeonatos']
            clube.campeonatos.set(campeonatos)  # Define os campeonatos associados
            return redirect('clube_list')
    else:
        form = ClubeForm()
    return render(request, 'clubes/formClube.html', {'form': form})


def clube_update(request, id):
    clube = get_object_or_404(Clube, id=id)
    if request.method == 'POST':
        form = ClubeForm(request.POST, instance=clube)
        if form.is_valid():
            clube = form.save()  # Salva o clube
            campeonatos = form.cleaned_data['campeonatos']
            clube.campeonatos.set(campeonatos)  # Atualiza os campeonatos
            return redirect('clube_list')
    else:
        form = ClubeForm(instance=clube)
    return render(request, 'clubes/formClube.html', {'form': form})


def clube_delete(request, id):
    clube = get_object_or_404(Clube, id=id)
    if request.method == 'POST':
        clube.delete()
        return redirect('clube_list')
    return render(request, 'clubes/deleteClube.html', {'clube': clube})

# ========================== JOGADOR =======================================

def jogador_list(request):
    jogadores = Jogador.objects.all()
    return render(request, 'jogadores/listaJogador.html', {'jogadores': jogadores})


def jogador_create(request):
    if request.method == 'POST':
        form = JogadorForm(request.POST)
        if form.is_valid():
            jogador = form.save(commit=False)  # Salva sem comitar para ajustes adicionais
            jogador.save()  # Salva o jogador
            clube = form.cleaned_data['clube']
            clube.jogadores.add(jogador)  # Associa o jogador ao clube
            return redirect('jogador_list')
    else:
        form = JogadorForm()
    return render(request, 'jogadores/formJogador.html', {'form': form})


def jogador_update(request, cpf):
    jogador = get_object_or_404(Jogador, cpf=cpf)
    if request.method == 'POST':
        form = JogadorForm(request.POST, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('jogadores/jogador_list')
    else:
        form = JogadorForm(instance=jogador)
    return render(request, 'jogadores/formJogador.html', {'form': form})


def jogador_delete(request, cpf):
    jogador = get_object_or_404(Jogador, cpf=cpf)
    if request.method == 'POST':
        jogador.delete()
        return redirect('jogadores/jogador_list')
    return render(request, 'jogadores/deleteJogador.html', {'jogador': jogador})


# ========================== JOGADOR =======================================
def treinador_list(request):
    treinadores = Treinador.objects.all()
    return render(request, 'treinadores/listaTreinador.html', {'treinadores': treinadores})

def treinador_create(request):
    if request.method == 'POST':
        form = TreinadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('treinador_list')
    else:
        form = TreinadorForm()
    return render(request, 'treinadores/formTreinador.html', {'form': form})

def treinador_update(request, cpf):
    treinador = get_object_or_404(Treinador, cpf=cpf)
    if request.method == 'POST':
       form = TreinadorForm(request.POST, instance=treinador)
       if form.is_valid():
           form.save()
           return redirect('treinador_list')
    else:
        form = TreinadorForm(instance=treinador)
    return render(request, 'treinadores/formTreinador.html', {'form': form})

def treinador_delete(request, cpf):
    treinador = get_object_or_404(Treinador, cpf=cpf)
    if request.method == 'POST':
        treinador.delete()
        return redirect('treinador_list')
    return render(request, 'treinadores/deleteTreinador.html', {'treinador': treinador})
