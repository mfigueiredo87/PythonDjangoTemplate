from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    form = LoginForms()
    return render(request, "usuarios/login.html", {"form":form})

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForms(request.POST)
        if form.is_valid():
            senha_1 = form.cleaned_data.get('senha_1')
            senha_2 = form.cleaned_data.get('senha_2')

            # Verifica se as senhas são iguais
            if senha_1 != senha_2:
                form.add_error('senha_2', 'As senhas não coincidem')
                return render(request, "usuarios/cadastro.html", {"form": form})

            nome = form.cleaned_data.get('nome_cadastro')
            email = form.cleaned_data.get('email')

            # Verifica se o nome de usuário já existe
            if User.objects.filter(username=nome).exists():
                form.add_error('nome_cadastro', 'Nome de usuário já existe')
                return render(request, "usuarios/cadastro.html", {"form": form})

            # Cria o usuário
            User.objects.create_user(
                username=nome,
                email=email,
                password=senha_1
            )
            return redirect('login')
    else:
        form = CadastroForms()

    return render(request, "usuarios/cadastro.html", {"form": form})

def logout(request):
    return render(request, "usuarios/logout.html")