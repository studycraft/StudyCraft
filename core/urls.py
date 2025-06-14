from rest_framework import routers
from django.urls import path, include
from .views import (
    AlunoViewSet, ProfessorViewSet, TrilhaViewSet,
    index, login_aluno, login_professor, login_admin, dashboard_admin, cadastro_professor, 
    cadastro_aluno, cadastro_trilha, dashboard_data, painel_professor, cadastro_aventura, relatorio_engajamento,
    painel_aventuras, painel_progresso, listar_aventuras, avaliar_aventura1, avaliar_aventura2
)

router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'trilhas', TrilhaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # ✅ rotas de API
    
    # ✅ rotas de templates
    path('', index, name='index'),
    path('login/aluno/', login_aluno, name='login_aluno'),
    path('login/professor/', login_professor, name='login_professor'),
    path('login/admin/', login_admin, name='login_admin'),
    path('painel/admin/', dashboard_admin, name='dashboard_admin'),
    path('painel/professores/', cadastro_professor, name='cadastro_professor'),
    path('painel/alunos/', cadastro_aluno, name='cadastro_aluno'),
    path('painel/trilha/', cadastro_trilha, name='cadastro_trilha'),
    path('painel/professor/', painel_professor, name='dashboard_professor'),
    path('painel/professor/aventura/', cadastro_aventura, name='cadastro_aventura'),
    path('painel/professor/relatorio/', relatorio_engajamento, name='relatorio_engajamento'),
    path('painel/aluno/', painel_aventuras, name='painel_aventuras'),
    path('painel/aluno/progresso/', painel_progresso, name='painel_progresso'),
    path('professor/aventuras/', listar_aventuras, name='listar_aventura'),
    path('professor/aventura/avaliar/1/', avaliar_aventura1, name='avaliar_aventura1'),
    path('professor/aventura/avaliar/2/', avaliar_aventura2, name='avaliar_aventura2'),

]

urlpatterns += [
    path('api/admin/dashboard/', dashboard_data, name='dashboard_data'),
]