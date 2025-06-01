// admin.js

// ✅ Verifica se o usuário está logado
function verificarLogin() {
    const token = localStorage.getItem('access_token');  // ✅ corrigido

    if (!token) {
        alert('Você precisa estar logado!');
        window.location.href = '/login/admin/';  // ✅ corrigido
        return null;
    }
    return token;
}

// ✅ Função de logout
function logout() {
    localStorage.removeItem('access_token');  // ✅ corrigido
    alert('Logout realizado com sucesso!');
    window.location.href = '/login/admin/';  // ✅ corrigido
}

// ✅ Exibe mensagens de alerta dinâmicas
function exibirAlerta(mensagem, tipo = 'info') {
    const alerta = document.createElement('div');
    alerta.className = `alert alert-${tipo}`;
    alerta.innerHTML = `
        <span>${mensagem}</span>
        <button class="btn-close" onclick="this.parentElement.remove()">&times;</button>
    `;
    document.body.prepend(alerta);

    // Remove automaticamente após 5 segundos
    setTimeout(() => alerta.remove(), 5000);
}

function sairDoPainel() {
    localStorage.removeItem('access_token');
    alert('Logout realizado com sucesso!');
    window.location.href = '/';  // ✅ redireciona para a index
}
