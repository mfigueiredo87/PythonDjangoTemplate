from django.contrib import admin
from galeria.models import Fotografia
# Register your models here.

# definindo uma class para display dos dados
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id","nome","legenda")
    # adicionando links no display
    list_display_links = ("id","nome")
    # adicionando o campo de busca
    search_fields = ("nome",)
admin.site.register(Fotografia, ListandoFotografias)
