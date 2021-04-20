from django import forms
from django.forms import fields, widgets

from apps.libro.models import Libro

class LibroModelForm(forms.ModelForm):
    class Meta:
        model = Libro
        
        fields = [
            'titulo', 
            'autor', 
            'pais', 
            'año', 
            'editorial', 
            'edicion', 
            'resumen', 
            'tema',
            'link',
        ]
        labels = {
            'titulo':'Titulo del libro*', 
            'autor':'Autor*', 
            'pais':'Pais', 
            'año':'Año*', 
            'editorial':'Editorial', 
            'edicion':'Edición', 
            'resumen':'Resumen', 
            'tema':'Tema*',
            'link':'Enlace*',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'autor': forms.TextInput(attrs={'class':'form-control'}),
            'pais': forms.TextInput(attrs={'class':'form-control'}),
            'año': forms.TextInput(attrs={'class':'form-control'}),
            'editorial': forms.TextInput(attrs={'class':'form-control'}),
            'edicion': forms.TextInput(attrs={'class':'form-control'}),
            'resumen': forms.Textarea(attrs={'class':'form-control'}),
            'tema': forms.Select(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class':'form-control'}),
        }