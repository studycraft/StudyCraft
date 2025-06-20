from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Aluno, Professor, Trilha, Quiz, Questao, Resposta, ResultadoQuiz
from .serializers import AlunoSerializer, ProfessorSerializer, TrilhaSerializer, QuizSerializer, ResultadoQuizSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.utils.timezone import now
from django.db.models import Count

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

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save(professor=None)

    def perform_update(self, serializer):
        instance = serializer.save()
        ResultadoQuiz.objects.filter(quiz=instance).delete()

class ResultadoQuizViewSet(viewsets.ModelViewSet):
    queryset = ResultadoQuiz.objects.all()
    serializer_class = ResultadoQuizSerializer
    permission_classes = [IsAuthenticated]

# Páginas HTML
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

def painel_professor(request):
    return render(request, 'professor/dashboard.html')

def cadastro_aventura(request):
    return render(request, 'professor/cadastro-aventura.html')

def relatorio_engajamento(request):
    return render(request, 'professor/relatorio-engajamento.html')

def painel_aventuras(request):
    return render(request, 'aluno/painel-aventuras.html')

def painel_progresso(request):
    return render(request, 'aluno/painel-progresso.html')

def responder_quizz(request):
    return render(request, 'aluno/responder_quizz.html')

def listar_aventuras(request):
    return render(request, 'professor/listar-aventuras.html')

def avaliar_aventura1(request):
    return render(request, 'professor/avaliar-aventura1.html')

def avaliar_aventura2(request):
    return render(request, 'professor/avaliar-aventura2.html')

def criar_quiz(request):
    return render(request, 'professor/criar_quiz.html')

@api_view(['POST'])
@permission_classes([AllowAny])
def salvar_quiz_publico(request):
    try:
        if not request.content_type == 'application/json':
            return Response(
                {'status': 'error', 'message': 'Content-Type deve ser application/json'},
                status=415
            )
        
        data = request.data
        
        if not all(key in data for key in ['nome', 'disciplina', 'serie', 'questoes']):
            return Response(
                {'status': 'error', 'message': 'Dados incompletos'},
                status=400
            )
        
        quiz = Quiz.objects.create(
            nome=data['nome'],
            disciplina=data['disciplina'],
            serie=data['serie'],
            professor=None,
            publico=True
        )
        
        for questao_data in data['questoes']:
            questao = Questao.objects.create(
                quiz=quiz,
                texto=questao_data['texto'],
                pontos=questao_data['pontos'],
                ordem=questao_data.get('ordem', 1)
            )
            
            for resposta_data in questao_data['respostas']:
                Resposta.objects.create(
                    questao=questao,
                    texto=resposta_data['texto'],
                    correta=resposta_data['correta'],
                    ordem=resposta_data.get('ordem', 1)
                )
        
        return Response({
            'status': 'success',
            'quiz_id': quiz.id,
            'message': 'Quiz público salvo com sucesso!'
        }, status=201)
        
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        }, status=400)
        
# API Endpoints
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard_data(request):
    total_alunos = Aluno.objects.count()
    total_professores = Professor.objects.count()
    total_trilhas = Trilha.objects.count()
    total_quizzes = Quiz.objects.count()

    atividades = []
    if total_alunos > 0:
        atividades.append(f"{total_alunos} alunos cadastrados")
    if total_professores > 0:
        atividades.append(f"{total_professores} professores cadastrados")
    if total_trilhas > 0:
        atividades.append(f"{total_trilhas} trilhas registradas")
    if total_quizzes > 0:
        atividades.append(f"{total_quizzes} quizzes criados")

    atividades.append(f"Acesso em: {now().strftime('%d/%m/%Y %H:%M')}")

    return Response({
        'total_alunos': total_alunos,
        'total_professores': total_professores,
        'total_trilhas': total_trilhas,
        'total_quizzes': total_quizzes,
        'atividades': atividades
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_quizzes_usuario(request):
    user = request.user
    quizzes = Quiz.objects.filter(professor__user=user) if hasattr(user, 'professor') else Quiz.objects.all()
    serializer = QuizSerializer(quizzes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def obter_quiz_para_resposta(request, quiz_id):
    try:
        quiz = Quiz.objects.get(pk=quiz_id)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)
    except Quiz.DoesNotExist:
        return Response({'status': 'error', 'message': 'Quiz não encontrado'}, status=404)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submeter_resposta(request):
    try:
        aluno = request.user.aluno
        data = request.data
        
        quiz = Quiz.objects.get(pk=data['quiz_id'])
        pontuacao = 0
        
        for resposta_submetida in data['respostas']:
            questao = Questao.objects.get(pk=resposta_submetida['questao_id'])
            resposta = Resposta.objects.get(pk=resposta_submetida['resposta_id'])
            
            if resposta.correta:
                pontuacao += questao.pontos
        
        ResultadoQuiz.objects.create(
            aluno=aluno,
            quiz=quiz,
            pontuacao=pontuacao
        )
        
        return Response({'status': 'success', 'pontuacao': pontuacao})
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=400)

from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
def listar_resultados(request):
    quiz_id = request.GET.get('quiz_id')
    serie = request.GET.get('serie')
    disciplina = request.GET.get('disciplina')

    resultados = ResultadoQuiz.objects.select_related('aluno', 'quiz')

    if quiz_id:
        resultados = resultados.filter(quiz_id=quiz_id)
    if serie:
        resultados = resultados.filter(quiz__serie=serie)
    if disciplina:
        resultados = resultados.filter(quiz__disciplina=disciplina)

    resultados = resultados.order_by('-id')

    data = [
        {
            "aluno": {"nome": r.aluno.nome if r.aluno else 'Carlos Wanderson'},
            "quiz": {"nome": r.quiz.nome},
            "pontuacao": r.pontuacao,
        }
        for r in resultados
    ]
    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def quizzes_disponiveis(request):
    """Lista quizzes disponíveis para alunos responderem"""
    try:
        quizzes = Quiz.objects.filter(ativo=True).annotate(
            questoes_count=Count('questoes')
        ).values('id', 'nome', 'disciplina', 'serie', 'questoes_count')
        
        return Response(list(quizzes))
    
    except Exception as e:
        return Response(
            {'status': 'error', 'message': str(e)},
            status=500
        )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def detalhes_quiz(request, quiz_id):
    """Retorna detalhes completos de um quiz para resposta"""
    try:
        quiz = Quiz.objects.get(pk=quiz_id, ativo=True)
        serializer = QuizSerializer(quiz)
        return Response(serializer.data)
        
    except Quiz.DoesNotExist:
        return Response(
            {'status': 'error', 'message': 'Quiz não encontrado ou inativo'},
            status=404
        )
    except Exception as e:
        return Response(
            {'status': 'error', 'message': str(e)},
            status=500
        )

@api_view(['POST'])
@permission_classes([AllowAny])  # Permite envio sem autenticação
def enviar_respostas(request):
    """Processa as respostas de um quiz e salva no banco"""
    try:
        data = request.data

        quiz = Quiz.objects.get(pk=data['quiz_id'], ativo=True)
        pontuacao = 0

        for resposta_submetida in data['respostas']:
            questao = Questao.objects.get(pk=resposta_submetida['questao_id'], quiz=quiz)
            resposta = Resposta.objects.get(pk=resposta_submetida['resposta_id'], questao=questao)

            if resposta.correta:
                pontuacao += questao.pontos

        # ✅ SALVA o resultado no banco, mesmo sem aluno vinculado
        ResultadoQuiz.objects.create(
            quiz=quiz,
            pontuacao=pontuacao
        )

        return Response({
            'status': 'success',
            'pontuacao': pontuacao,
            'pontuacao_maxima': sum(q.pontos for q in quiz.questoes.all())
        })

    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=400)

