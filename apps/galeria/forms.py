from django import forms
from apps.galeria.models import Fotografia

class FotografiaForms(forms.ModelForm):
    # definindo metadados, dados que fazem referencia a propria classe
    class Meta:
        model = Fotografia
        
        # definir os inputs que serao excluidos ou nao visiveis
        exclude = ['publicado',]
        labels = {
            'descricao':'Descrição',
            'data_fotografia':'Data de Registo',
            'foto':'Fotografia',
            'nome':'Nome da Fotografia',
            'usuario':'Utilizador'
        }
        
         # definir os inputs do formulario
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda':forms.TextInput(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'descricao':forms.Textarea(attrs={'class':'form-control'}),
            'foto':forms.FileInput(attrs={'class':'form-control'}),
            'data_fotografia':forms.DateInput(
                format='%d/%m/%Y',
                attrs={
                    'type': 'date',
                    'class':'form-control'
                    }),
            'usuario':forms.Select(attrs={'class':'form-control'}),
        }