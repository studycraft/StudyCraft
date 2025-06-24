# StudyCraft

**Aprender nunca foi tão divertido!**

Plataforma gamificada de aprendizagem desenvolvida por estudantes da 16ª GRE - Pio IX, como solução educacional para o Seduckathon. A proposta transforma tarefas escolares em aventuras, estimulando o engajamento por meio de trilhas, pontuações, rankings e recompensas.

---

## 🎯 Objetivo

Combater o desinteresse escolar com uma ferramenta inovadora, acessível e divertida, integrando recursos de gamificação ao processo educacional.

## 📄 Documentos do Projeto

- 📘 [Documentação Técnica - Projeto StudyCraft (PDF)](./docs/Documentacao_Tecnica_StudyCraft.pdf)  
- 🎤 [Apresentação Pitch - CETI Nossa Senhora do Patrocínio (PDF)](./docs/Pitch_CETI_Nossa_Senhora_do_Patrocinio.pdf)

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

> ⚠️ **Pré-requisitos:**
- Python 3.11 instalado
- Git instalado
- Navegador moderno (Chrome, Firefox, etc.)

---

### 1. Clone o repositório

```bash
git clone https://github.com/studycraft/StudyCraft.git
cd StudyCraft
```

---

### 2. Crie e ative o ambiente virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

Se, ao ativar o ambiente, aparecer um erro como:
```
execution of scripts is disabled on this system
```

Execute o seguinte comando no PowerShell (como usuário normal):

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Quando solicitado, digite `A` (Yes to All) ou `Y` para confirmar.

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Instale as dependências do projeto

```bash
pip install -r requirements.txt
```

---

### 4. Rode o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse o sistema em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Para acessar em qualquer perfil utilize as seguintes credenciais de superusuário:

  ```
  Usuário: admin
  Senha: 123456
  ```

---

### ✅ Dicas Úteis

- O sistema é **100% local** e funciona sem internet.
- O banco de dados padrão (SQLite) **já está incluído no repositório**, pronto para uso.
- Você **só precisa rodar `migrate`** se:
  - Excluir o arquivo `db.sqlite3`, ou
  - Clonar o projeto e ele **não vier com o banco de dados** incluído.

Se esse for o caso, ative o ambiente virtual e execute:

```bash
python manage.py migrate
```

- Se faltar alguma biblioteca, ative o ambiente virtual e repita:

```bash
pip install -r requirements.txt
```

- O projeto não exige nenhuma configuração adicional — basta rodar o servidor e acessar [http://127.0.0.1:8000](http://127.0.0.1:8000)


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

Este projeto é de propriedade da equipe StudyCraft.  
O uso, cópia, distribuição ou modificação do sistema só é permitido mediante contrato de licença com os autores.  
Para parcerias ou aquisição comercial, entre em contato com a equipe responsável.

studycraft.2025@gmail.com
