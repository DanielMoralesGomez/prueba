from django.shortcuts import render
from rest_framework import viewsets,filters
from app.estudiante.models import Estudiante
from app.estudiante.serializers import EstudianteSerializer
from django_filters.rest_framework import DjangoFilterBackend

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
    ]
    filterset_fields = ('__all__')
    search_fields = ('__all__')
