from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid

class Usuario(AbstractUser):
    pass

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    matricula = models.CharField(max_length=10, unique=True)
    disciplina = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    ra = models.CharField(max_length=20, unique=True)
    turma = models.CharField(max_length=50)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.turma}"

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

Usuario = get_user_model()

# Adicione estes campos ao modelo Quiz
class Quiz(models.Model):
    nome = models.CharField(max_length=100)
    disciplina = models.CharField(max_length=50)
    serie = models.CharField(max_length=10)
    professor = models.ForeignKey(
        Professor, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    publico = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)  # Novo campo para controle de status

    class Meta:
        verbose_name_plural = "Quizzes"
        ordering = ['-data_criacao']

    def __str__(self):
        return self.nome
    
    @property
    def questoes_count(self):
        return self.questoes.count()
    
class Questao(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questoes')
    texto = models.TextField()
    pontos = models.IntegerField(default=1)
    ordem = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.texto[:50]}..." if len(self.texto) > 50 else self.texto

class Resposta(models.Model):
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE, related_name='respostas')
    texto = models.CharField(max_length=255)
    correta = models.BooleanField(default=False)
    ordem = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.texto} {'(Correta)' if self.correta else ''}"

class ResultadoQuiz(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    pontuacao = models.IntegerField()
    
class Meta:
    verbose_name_plural = "Resultados de Quiz"
    ordering = ['-pontuacao']

    
    def __str__(self):
        return f"{self.aluno.nome} - {self.quiz.nome}: {self.pontuacao} pts"