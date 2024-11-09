# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter # type: ignore
from .views import CampeonatoViewSet, jogador_list, jogador_create, jogador_update, jogador_delete

router = DefaultRouter()
router.register(r'campeonatos', CampeonatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('jogadores/', jogador_list, name='jogador_list'),
    path('jogadores/novo/', jogador_create, name='jogador_create'),
    path('jogadores/<str:cpf>/editar/', jogador_update, name='jogador_update'),
    path('jogadores/<str:cpf>/deletar/', jogador_delete, name='jogador_delete'),
]
