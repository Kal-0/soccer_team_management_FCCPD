from django.shortcuts import render
from rest_framework import viewsets
from .models import Campeonato
from .serializers import CampeonatoSerializer

class CampeonatoViewSet(viewsets.ModelViewSet):
    queryset = Campeonato.objects.all()
    serializer_class = CampeonatoSerializer
