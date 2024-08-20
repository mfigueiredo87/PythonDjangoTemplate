from django.urls import path
from galeria.views import index

# criar a lista para manter os endpoints do app galeria
urlpatterns = [
    path('', index)
    
]