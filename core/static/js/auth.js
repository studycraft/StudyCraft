async function login(username, password, redirectUrl) {
    try {
        const response = await fetch(`${window.location.origin}/api/token/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        if (!response.ok) {
            throw new Error('Login falhou: ' + response.status);
        }

        const data = await response.json();

        localStorage.setItem('access_token', data.access);
        localStorage.setItem('refresh_token', data.refresh);

        alert('Login realizado com sucesso!');
        window.location.href = redirectUrl;

    } catch (error) {
        alert('Erro no login: ' + error.message);
    }
}

// Aluno
const alunoForm = document.getElementById('loginAluno');
if (alunoForm) {
    alunoForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('ra').value;
        const password = document.getElementById('senha').value;
        login(username, password, '/painel/aluno/');
    });
}

// Professor
const professorForm = document.getElementById('loginProfessor');
if (professorForm) {
    professorForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('matricula').value;
        const password = document.getElementById('senha').value;
        login(username, password, '/painel/professor/');
    });
}

// Admin
const adminForm = document.getElementById('loginAdmin');
if (adminForm) {
    adminForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('matricula').value;
        const password = document.getElementById('senha').value;
        login(username, password, '/painel/admin/');
    });
}
