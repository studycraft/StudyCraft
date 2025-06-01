from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Aluno, Professor, Trilha

Usuario = get_user_model()

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    nome = serializers.CharField()
    email = serializers.EmailField(write_only=True)
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Professor
        fields = ['id', 'nome', 'email', 'senha', 'matricula', 'disciplina']

    def create(self, validated_data):
        nome = validated_data.pop('nome')
        email = validated_data.pop('email')
        senha = validated_data.pop('senha')
        matricula = validated_data.get('matricula')
        disciplina = validated_data.get('disciplina')

        user = Usuario.objects.create_user(
            username=matricula,
            first_name=nome,
            email=email,
            password=senha
        )

        return Professor.objects.create(
            nome=nome,              # <--- Salva no Professor também!
            user=user,
            matricula=matricula,
            disciplina=disciplina
        )


    def update(self, instance, validated_data):
        nome = validated_data.pop('nome', None)
        email = validated_data.pop('email', None)
        senha = validated_data.pop('senha', None)
        matricula = validated_data.get('matricula')
        disciplina = validated_data.get('disciplina')

        user = instance.user
        if nome:
            user.first_name = nome
            instance.nome = nome      # <--- Atualiza nome do Professor!
        if email:
            user.email = email
        if senha:
            user.set_password(senha)
        user.username = matricula
        user.save()

        instance.matricula = matricula
        instance.disciplina = disciplina
        instance.save()

        return instance



class TrilhaSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer(read_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(
        queryset=Professor.objects.all(), source='professor', write_only=True
    )

    alunos = AlunoSerializer(many=True, read_only=True)
    alunos_ids = serializers.PrimaryKeyRelatedField(
        queryset=Aluno.objects.all(), many=True, source='alunos', write_only=True
    )

    class Meta:
        model = Trilha
        fields = ['id', 'nome', 'disciplina', 'professor', 'professor_id', 'alunos', 'alunos_ids', 'descricao']
