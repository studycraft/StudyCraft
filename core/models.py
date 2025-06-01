from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Usuario(AbstractUser):
    # Campos extras podem ser adicionados futuramente
    pass

class Professor(models.Model):
    nome = models.CharField(max_length=100)  # <-- Novo campo!
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    matricula = models.CharField(max_length=10, unique=True)
    disciplina = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    ra = models.CharField(max_length=20, unique=True)
    turma = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} - {self.turma}"

class Trilha(models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='trilhas')
    alunos = models.ManyToManyField(Aluno, blank=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
