from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

# Create your views here.
def login(request):
    # Cria uma instância do formulário
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            # Usa cleaned_data para obter os valores de forma segura
            nome = form.cleaned_data['nome_login']
            senha = form.cleaned_data['senha']
            
            usuario = auth.authenticate(
                request, 
                username=nome,
                password=senha
            )
            
            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request, f"Utilizador {nome} logado com sucesso!")
                return redirect('index')
            
            else:
                # Adiciona uma mensagem de erro ao formulário se a autenticação falhar
                messages.error(request, "Nome de usuário ou senha inválidos.")
                return redirect('login')
    
    # Renderiza o formulário com erros (se houver) ou em seu estado inicial
    return render(request, "usuarios/login.html", {"form": form})

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            senha_1 = form.cleaned_data.get('senha_1')
            senha_2 = form.cleaned_data.get('senha_2')

            # Verifica se as senhas são iguais
            if senha_1 != senha_2:
                messages.error(request, "As senhas não coincidem.")
                return render(request, "usuarios/cadastro.html", {"form": form})

            nome = form.cleaned_data.get('nome_cadastro')
            email = form.cleaned_data.get('email')

            # Verifica se o nome de usuário já existe
            if User.objects.filter(username=nome).exists():
                messages.error(request, "Nome de usuário já existe.")
                # form.add_error('nome_cadastro', 'Nome de usuário já existe')
                return render(request, "usuarios/cadastro.html", {"form": form})

            # Cria o usuário
            User.objects.create_user(
                username=nome,
                email=email,
                password=senha_1
            )
            messages.success(request, "Usuário cadastrado com sucesso.")
            return redirect('login')
    else:
        form = CadastroForms()

    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efectuado com sucesso.")
    return redirect('login')
