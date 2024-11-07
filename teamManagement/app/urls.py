# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CampeonatoViewSet

router = DefaultRouter()
router.register(r'campeonatos', CampeonatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
