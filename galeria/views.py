from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia
# Create your views here.

def index(request):
    # estruturas de dados ou dicionario
    fotografias = Fotografia.objects.all()
   

    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografias = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html',{"fotografias":fotografias})
