from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Aluno, Professor, Trilha
from .serializers import AlunoSerializer, ProfessorSerializer, TrilhaSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils.timezone import now

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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_data(request):
    total_alunos = Aluno.objects.count()
    total_professores = Professor.objects.count()
    total_trilhas = Trilha.objects.count()

    # Exemplo simples de "atividades recentes"
    atividades = []

    if total_alunos > 0:
        atividades.append(f"{total_alunos} alunos cadastrados")
    if total_professores > 0:
        atividades.append(f"{total_professores} professores cadastrados")
    if total_trilhas > 0:
        atividades.append(f"{total_trilhas} trilhas registradas")

    atividades.append(f"Acesso em: {now().strftime('%d/%m/%Y %H:%M')}")

    return Response({
        'total_alunos': total_alunos,
        'total_professores': total_professores,
        'total_trilhas': total_trilhas,
        'atividades': atividades
    })
