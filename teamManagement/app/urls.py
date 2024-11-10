from django.urls import path
from .views import home, campeonato_menu
from .views import campeonato_list, campeonato_create, campeonato_update, campeonato_delete
from .views import clube_list, clube_create, clube_update, clube_delete
from .views import jogador_list, jogador_create, jogador_update, jogador_delete
from .views import treinador_list, treinador_create, treinador_update, treinador_delete
from .views import medico_list, medico_create, medico_update, medico_delete

urlpatterns = [
     
     path('', home, name='home'),
     path('menu/campeonatos/', campeonato_menu, name='campeonato_menu'),
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
    
     path('treinadores/', treinador_list, name='treinador_list'),
     path('treinadores/novo/', treinador_create, name='treinador_create'),
     path('treinadores/editar/<str:cpf>/', treinador_update, name = 'treinador_update'),
     path('treinadores/editar/<str:cpf>/', treinador_delete, name = 'treinador_delete'),

     path('medicos/', medico_list, name='medico_list'),
     path('medicos/novo/', medico_create, name='medico_create'),
     path('medicos/editar/<int:id>/', medico_update, name='medico_update'),
     path('medicos/deletar/<int:id>/', medico_delete, name='medico_delete'),

]
