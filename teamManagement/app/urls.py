from django.urls import path
from .views import campeonato_list, campeonato_create, campeonato_update, campeonato_delete
from .views import clube_list, clube_create, clube_update, clube_delete
from .views import jogador_list, jogador_create, jogador_update, jogador_delete

urlpatterns = [
    path('campeonatos/', campeonato_list, name='campeonato_list'),
    path('campeonatos/novo/', campeonato_create, name='campeonato_create'),
    path('campeonatos/editar/<int:id>/',
         campeonato_update, name='campeonato_update'),
    path('campeonatos/deletar/<int:id>/',
         campeonato_delete, name='campeonato_delete'),
    path('clubes/', clube_list, name='clube_list'),
    path('clubes/novo/', clube_create, name='clube_create'),
    path('clubes/editar/<int:id>/', clube_update, name='clube_update'),
    path('clubes/deletar/<int:id>/', clube_delete, name='clube_delete'),
    path('jogadores/', jogador_list, name='jogador_list'),
    path('jogadores/novo/', jogador_create, name='jogador_create'),
    path('jogadores/<str:cpf>/editar/', jogador_update, name='jogador_update'),
    path('jogadores/<str:cpf>/deletar/', jogador_delete, name='jogador_delete'),
]