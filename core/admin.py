from django.contrib import admin
from .models import Usuario, Professor, Aluno, Trilha

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')

@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_nome', 'matricula', 'disciplina')

    def get_nome(self, obj):
        return obj.user.get_full_name() or obj.user.username
    get_nome.short_description = 'Nome'

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ra', 'turma')

@admin.register(Trilha)
class TrilhaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'disciplina', 'professor')
