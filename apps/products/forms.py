from django import forms 
from .models import Producto

class ProductoForm(forms.ModelForm): 
    class Meta: 
        model = Producto 
        fields = ['nombre', 'precio', 'descripcion', 'activo']


        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 100%;',
                'placeholder': 'Nombre'
                }),
            'precio': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 100%;',
                'placeholder': 'Precio'
                }),
            'descripcion': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 100%;',
                'placeholder': 'Descripción',
                'rows':4
                }),
            'activo': forms.CheckboxInput(attrs={
                'class': "form-check-input",
                'type': "checkbox",
                'placeholder': 'Estado'
                })
            }