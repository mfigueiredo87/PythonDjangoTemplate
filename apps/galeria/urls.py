from django.urls import path
from apps.galeria.views import index, imagem, buscar

# criar a lista para manter os endpoints do app galeria
urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path("buscar", buscar, name="buscar")
]