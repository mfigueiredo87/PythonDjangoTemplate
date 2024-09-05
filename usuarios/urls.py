from django.urls import path
from usuarios.views import login, cadastro, logout

# criar a lista para manter os endpoints do app usuasrios
urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout')
]