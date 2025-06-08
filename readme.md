# 📚 StudyCraft

StudyCraft é uma plataforma gamificada de ensino desenvolvida para engajar estudantes com base em missões, trilhas, rankings e recompensas. A aplicação utiliza Django (backend com DRF) e HTML/CSS/JS (frontend), com foco em acessibilidade e aplicação em escolas públicas.

---

## 📁 Estrutura do Projeto

A seguir, uma síntese das principais pastas e arquivos do projeto:

```
.
├── db.sqlite3               # Banco de dados local (SQLite, usado para testes e desenvolvimento)
├── manage.py                # Utilitário de linha de comando do Django para gerenciar o projeto
├── requirements.txt         # Lista de dependências Python do projeto
│
├── studycraft_backend/      # Configurações principais do projeto Django
│   ├── settings.py          # Configurações globais (apps, middleware, banco, static, etc.)
│   ├── urls.py              # Roteamento principal da aplicação
│   ├── asgi.py / wsgi.py    # Pontos de entrada para servidores ASGI/WSGI
│
├── core/                    # Aplicação principal da lógica do projeto
│   ├── models.py            # Modelos de dados (Aluno, Professor, Trilha, etc.)
│   ├── serializers.py       # Serializadores DRF para conversão entre JSON e modelos
│   ├── views.py             # Views que tratam as requisições e lógica da API
│   ├── urls.py              # Rotas específicas do app `core`
│   ├── admin.py             # Registro de modelos no painel administrativo do Django
│   ├── migrations/          # Histórico de versões do banco de dados
│   ├── static/              # Arquivos estáticos (CSS, JS, imagens)
│   │   ├── css/             # Estilos personalizados por tipo de usuário (admin, aluno, etc.)
│   │   ├── js/              # Scripts JS específicos para autenticação e interações
│   │   └── images/          # Logos e recursos visuais
│   ├── templates/           # Páginas HTML organizadas por tipo de usuário
│   │   ├── login/           # Telas de login para aluno, professor e admin
│   │   ├── admin/           # Dashboard e cadastros (aluno, professor, trilha)
│   │   ├── aluno/           # Painéis de aventuras e progresso do aluno
│   │   └── professor/       # Dashboard e ferramentas do professor
│
├── venv/                    # Ambiente virtual Python com bibliotecas instaladas
```

---

## 🚀 Tecnologias Utilizadas

- **Backend**: Django + Django REST Framework
- **Frontend**: HTML5, CSS3, JavaScript
- **Banco de Dados**: SQLite (desenvolvimento)
- **Autenticação**: JWT (JSON Web Token)
- **Outros**: Ambiente virtual (`venv`), estrutura modular e DRY

---

## 🧩 Funcionalidades (em desenvolvimento)

- Cadastro e login para alunos, professores e coordenação
- Painel do aluno com progresso, aventuras e ranking
- Painel do professor com visualização de engajamento e criação de trilhas
- Dashboard da coordenação com gerenciamento de usuários e trilhas
- Sistema de recompensas baseado em missões escolares

---

## 📌 Observações

- Toda a lógica de cadastro e manipulação de dados está conectada à API RESTful.
- O projeto está em desenvolvimento no contexto do **2º SEDUCKATHON** com foco em escolas públicas do Piauí.
