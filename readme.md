# StudyCraft

**Aprender nunca foi tão divertido!**

Plataforma gamificada de aprendizagem desenvolvida por estudantes da 16ª GRE - Pio IX, como solução educacional para o Seduckathon. A proposta transforma tarefas escolares em aventuras, estimulando o engajamento por meio de trilhas, pontuações, rankings e recompensas.

---

## 🎯 Objetivo

Combater o desinteresse escolar com uma ferramenta inovadora, acessível e divertida, integrando recursos de gamificação ao processo educacional.

---

## 🚀 Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python 3.11, Django, Django REST Framework
- **Autenticação**: JWT (JSON Web Token)
- **Banco de Dados**: SQLite (modo local) / PostgreSQL (produção)
- **APIs**: RESTful

---

## 🧱 Estrutura do Projeto

```bash
studycraft/
├── core/                  # Lógica principal do backend
│   ├── models.py          # Modelos: Aluno, Professor, Trilha, Aventura
│   ├── views.py           # ViewSets e lógicas da API
│   ├── serializers.py     # Serializadores DRF
│   └── urls.py            # Rotas da aplicação
├── static/                # Arquivos estáticos (CSS, JS, imagens, PDFs)
│   ├── css/
│   ├── js/
│   ├── images/
│   └── pdfs/
├── templates/             # Frontend HTML
│   ├── admin/             # Telas de coordenação
│   ├── aluno/             # Telas do aluno
│   ├── professor/         # Telas do professor
│   └── login/             # Telas de autenticação
├── db.sqlite3             # Banco local (desenvolvimento)
└── manage.py              # Gerenciador Django
```

---

## 📚 Funcionalidades

- Autenticação de Aluno, Professor e Coordenação
- Cadastro de trilhas e aventuras (tarefas)
- Upload/download de PDFs de atividades
- Registro de entregas de alunos
- Barra de progresso e pontuação por recompensa
- Interface responsiva e acessível

---

## 🔐 Autenticação (JWT)

Endpoint de login:
```http
POST /api/token/
Body: {
  "username": "usuario",
  "password": "senha"
}
```

Headers para autenticação:
```
Authorization: Bearer <access_token>
```

---

## 🔄 Endpoints da API (exemplos)

| Método | Rota                  | Descrição                   |
|--------|-----------------------|-----------------------------|
| POST   | /api/token/           | Login (retorna JWT)         |
| GET    | /api/alunos/          | Lista de alunos             |
| GET    | /api/professores/     | Lista de professores        |
| GET    | /api/trilhas/         | Lista de trilhas educacionais |
| POST   | /api/aventuras/       | Criação de nova aventura    |

---

## ▶️ Executando localmente

```bash
# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações
python manage.py migrate

# Rode o servidor
python manage.py runserver
```

Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 👥 Equipe (16ª GRE - CETI Nossa Senhora do Patrocínio)

- Amanda Rafaela Batista Arrais
- Carlos Wanderson Ferreira de Sousa Sudário
- Francisco Rodrigo da Silva
- Maria Beatriz dos Santos Silva
- Maria Yasmin Alves

**Orientador:** Prof. José Diógenes Vieira da Costa

---

## 🏁 Status

🟢 Em desenvolvimento. Funcionalidades principais operacionais. Integração dinâmica das telas de aluno e professor em andamento.

---

## 📜 Licença

Projeto educacional de uso público. Livre para replicação em escolas e iniciativas sociais.
