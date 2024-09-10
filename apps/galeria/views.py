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
            
            
    return render(request, 'galeria/buscar.html', {"cards":fotografias})

# metodos para as imagens
def nova_imagem(request):
    form = FotografiaForms
    return render(request, 'galeria/nova_imagem.html', {'form':form})

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass