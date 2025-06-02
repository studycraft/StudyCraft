from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

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

import uuid
from django.db import models
from .models import Professor  # certifique-se de importar

class Trilha(models.Model):
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True, editable=False, blank=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='trilhas')
    descricao = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.codigo:
            unique = uuid.uuid4().hex[:6].upper()
            self.codigo = f'TRI-{unique}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome} - {self.codigo}"
    
    @property
    def disciplina(self):
        return self.professor.disciplina


