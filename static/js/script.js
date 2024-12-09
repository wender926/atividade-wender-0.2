// Função de login corrigida
function login(event) {
    event.preventDefault();  // Evita envio padrão
    
    const email = document.getElementById("email_login").value;
    const senha = document.getElementById("senha_login").value;



    // Verifica se o usuário existe
    const usuarioEncontrado = usuariosCadastrados.find(
        (usuario) => usuario.email === email && usuario.senha === senha
    );

    if (usuarioEncontrado) {
        // Redireciona para "home.html"
        window.location.href = `home.html?mensagem=Login com sucesso, ${usuarioEncontrado.nome}!`;
    } else {
        alert("Email ou senha incorretos. Tente novamente.");
    }
}
