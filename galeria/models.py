from django.db import models

# Create your models here.
# criar as classes para o banco de dados/tabelas no banco
class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    
    # funcao que devolver o nome de cada item
    def __str__(self):
        return f"Fotografia [nome={self.nome}]"
    