from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia
# Create your views here.

def index(request):
    # estruturas de dados ou dicionario
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicado=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografias = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografias":fotografias})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicado=True)
   
    #  filtrar a palavra da busca
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        # conferir se conseguiu algum nome
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
            
            
    return render(request, 'galeria/buscar.html', {"cards":fotografias})