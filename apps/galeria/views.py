from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms

from django.contrib import messages

# Create your views here.

def index(request):
    # verificar se o user n ta logado e mandar para o login
    if not request.user.is_authenticated:
        messages.error(request, "Usuario nao logado. Faça Login para ter acesso")
        return redirect('login')
    # estruturas de dados ou dicionario
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicado=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografias = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografias":fotografias})

def buscar(request):
     # verificar se o user n ta logado e mandar para o login
    if not request.user.is_authenticated:
        messages.error(request, "Usuario nao logado. Faça Login para ter acesso")
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicado=True)
   
    #  filtrar a palavra da busca
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        # conferir se conseguiu algum nome
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
            
            
    return render(request, 'galeria/index.html', {"cards":fotografias})

# metodos para as imagens
def nova_imagem(request):
     # verificar se o user n ta logado e mandar para o login
    if not request.user.is_authenticated:
        messages.error(request, "Usuario não logado. Faça Login para ter acesso")
        return redirect('login')
    
    form = FotografiaForms
    if request.method=='POST':
        form = FotografiaForms(request.POST, request.FILES)
        # validar o formulario
        if form.is_valid():
            form.save()
        messages.success(request, "Fotografia cadastrada com sucesso.")
        return redirect('index')
    
    return render(request, 'galeria/nova_imagem.html', {'form':form})

def editar_imagem(request, foto_id):
    # capturar as informacos do banco
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)
    # confirmar o metodo recebido e incluir os dados de request no formulario
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
        # verificar se o formulario eh valido
        if form.is_valid():
            form.save()
        messages.success(request, "Fotografia editada com sucesso.")
        return redirect('index')
    
    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id':foto_id})
    

def deletar_imagem(request, foto_id):
    # pegar as informacoes da fotografia a editar
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, "Fotografia apagada com sucesso.")
    return redirect('index')

# filtro de categorias
def filtro(request, categoria):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicado=True, categoria=categoria)
    return render(request, 'galeria/index.html', {"cards": fotografias})



    