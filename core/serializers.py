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
    email = serializers.EmailField(source='user.email')  # <-- aqui está a correção
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Professor
        fields = ['id', 'nome', 'email', 'senha', 'matricula', 'disciplina']

    def create(self, validated_data):
        nome = validated_data.pop('nome')
        senha = validated_data.pop('senha')
        user_data = validated_data.pop('user')
        email = user_data.get('email')
        matricula = validated_data.get('matricula')
        disciplina = validated_data.get('disciplina')

        user = Usuario.objects.create_user(
            username=matricula,
            first_name=nome,
            email=email,
            password=senha
        )

        return Professor.objects.create(
            nome=nome,
            user=user,
            matricula=matricula,
            disciplina=disciplina
        )

    def update(self, instance, validated_data):
        nome = validated_data.pop('nome', None)
        senha = validated_data.pop('senha', None)
        user_data = validated_data.pop('user', {})
        email = user_data.get('email', None)

        user = instance.user
        if nome:
            user.first_name = nome
            instance.nome = nome
        if email:
            user.email = email
        if senha:
            user.set_password(senha)
        user.username = validated_data.get('matricula', user.username)
        user.save()

        instance.matricula = validated_data.get('matricula', instance.matricula)
        instance.disciplina = validated_data.get('disciplina', instance.disciplina)
        instance.save()

        return instance




class TrilhaSerializer(serializers.ModelSerializer):
    professor = ProfessorSerializer(read_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(
        queryset=Professor.objects.all(), source='professor', write_only=True
    )
    disciplina = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Trilha
        fields = ['id', 'nome', 'codigo', 'disciplina', 'professor', 'professor_id', 'descricao']
        read_only_fields = ['codigo']

    def get_disciplina(self, obj):
        return obj.professor.disciplina if obj.professor else ''

