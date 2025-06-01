from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Aluno, Professor, Trilha
from .serializers import AlunoSerializer, ProfessorSerializer, TrilhaSerializer

# API Views
class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [IsAuthenticated]

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated]

class TrilhaViewSet(viewsets.ModelViewSet):
    queryset = Trilha.objects.all()
    serializer_class = TrilhaSerializer
    permission_classes = [IsAuthenticated]

# Páginas HTML (renderizadas pelo Django)
def index(request):
    return render(request, 'index.html')

def login_aluno(request):
    return render(request, 'login/aluno.html')

def login_professor(request):
    return render(request, 'login/professor.html')

def login_admin(request):
    return render(request, 'login/admin.html')

def dashboard_admin(request):
    return render(request, 'admin/dashboard.html')

def cadastro_professor(request):
    return render(request, 'admin/cadastro-professor.html')

def cadastro_aluno(request):
    return render(request, 'admin/cadastro-aluno.html')

def cadastro_trilha(request):
    return render(request, 'admin/cadastro-trilha.html')
