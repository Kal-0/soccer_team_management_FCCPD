from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/campeonatos/', views.campeonato_menu, name='campeonato_menu'),
    
    # URLs para campeonatos
    path('campeonatos/', views.campeonato_list, name='campeonato_list'),
    path('campeonatos/novo/', views.campeonato_create, name='campeonato_create'),
    path('campeonatos/editar/<int:id>/', views.campeonato_update, name='campeonato_update'),
    path('campeonatos/deletar/<int:id>/', views.campeonato_delete, name='campeonato_delete'),
    
    # URLs para clubes
    path('clubes/', views.clube_list, name='clube_list'),
    path('clubes/novo/', views.clube_create, name='clube_create'),
    path('clubes/editar/<int:id>/', views.clube_update, name='clube_update'),
    path('clubes/deletar/<int:id>/', views.clube_delete, name='clube_delete'),
    
    # URLs para jogadores
    path('jogadores/', views.jogador_list, name='jogador_list'),
    path('jogadores/novo/', views.jogador_create, name='jogador_create'),
    path('jogadores/<str:cpf>/editar/', views.jogador_update, name='jogador_update'),
    path('jogadores/<str:cpf>/deletar/', views.jogador_delete, name='jogador_delete'),
    
    # URLs para treinadores
    path('treinadores/', views.treinador_list, name='treinador_list'),
    path('treinadores/novo/', views.treinador_create, name='treinador_create'),
    path('treinadores/editar/<str:cpf>/', views.treinador_update, name='treinador_update'),
    path('treinadores/deletar/<str:cpf>/', views.treinador_delete, name='treinador_delete'),
    
    # URLs para médicos
    path('medicos/', views.medico_list, name='medico_list'),
    path('medicos/novo/', views.medico_create, name='medico_create'),
    path('medicos/editar/<int:id>/', views.medico_update, name='medico_update'),
    path('medicos/deletar/<int:id>/', views.medico_delete, name='medico_delete'),
    
    #URLs consultas
    path('consultas/', views.consulta_list, name='consulta_list'),
    path('jogadores_clubes_campeonatos/', views.jogadores_clubes_campeonatos, name='jogadores_clubes_campeonatos'),
    path('treinadores_medicos_por_clube/', views.treinadores_medicos_por_clube, name='treinadores_medicos_por_clube'),
    path('clubes_campeonatos_datas/', views.clubes_campeonatos_datas, name='clubes_campeonatos_datas'),
]
