from django.contrib import admin
from galeria.models import Fotografia
# Register your models here.

# definindo uma class para display dos dados
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id","nome","legenda","publicado")
    # adicionando links no display
    list_display_links = ("id","nome")
    # adicionando o campo de busca
    search_fields = ("nome",)
    # criar filtros por categorias
    list_filter = ("categoria",)
    # para mostrar o checkbox para publicacao
    list_editable = ("publicado",)
    # paginacao
    list_per_page = 10
admin.site.register(Fotografia, ListandoFotografias)
