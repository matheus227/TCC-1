function mostrarLogin(tipo) {
    document.getElementById('login-container').style.display = 'block';
    document.getElementById('login-aluno').style.display = tipo === 'aluno' ? 'block' : 'none';
    document.getElementById('login-bibliotecario').style.display = tipo === 'bibliotecario' ? 'block' : 'none';
    document.getElementById('cadastro-aluno').style.display = 'none';
}

function mostrarCadastroAluno() {
    document.getElementById('login-aluno').style.display = 'none';
    document.getElementById('cadastro-aluno').style.display = 'block';
}

function loginAluno() {
    let nome = document.getElementById('aluno-nome').value;
    let senha = document.getElementById('aluno-senha').value;
    let alunos = JSON.parse(localStorage.getItem('alunos')) || [];
    let aluno = alunos.find(a => a.nome === nome && a.senha === senha);
    
    if (aluno) {
        alert('Login bem-sucedido!');
        document.getElementById('login-container').style.display = 'none';
        document.getElementById('area-aluno').style.display = 'block';
    
    } else {
        alert('Nome ou senha incorretos!');
    }
}

function cadastrarAluno() {
    let nome = document.getElementById('novo-aluno-nome').value;
    let senha = document.getElementById('novo-aluno-senha').value;
    let serie = document.getElementById('aluno-serie').value;
    let alunos = JSON.parse(localStorage.getItem('alunos')) || [];
    
    alunos.push({ nome, senha, serie });
    localStorage.setItem('alunos', JSON.stringify(alunos));
    alert('Cadastro realizado com sucesso!');
    mostrarLogin('aluno');
}

function loginBibliotecario() {
    let usuario = document.getElementById('bibliotecario-usuario').value;
    let senha = document.getElementById('bibliotecario-senha').value;
    
    if (usuario === 'bibliotecario' && senha === 'autorizado1234') {
        alert('Login bem-sucedido!');
        document.getElementById('login-container').style.display = 'none';
        document.getElementById('area-bibliotecario').style.display = 'block';
    } else {
        alert('Usuário ou senha incorretos!');
    }
}



