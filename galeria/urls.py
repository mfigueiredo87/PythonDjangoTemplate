from django.urls import path
from galeria.views import index, imagem

# criar a lista para manter os endpoints do app galeria
urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
    
]