from django import forms

from .models import Reserva, Clase


class ReservaSearchForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre de usuario")


class ReservaCreateForm(forms.Form):
    nombre_de_usuario = forms.CharField(max_length=50, required=True, label="Ingresar nombre del alumno")


class ClaseCreateForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = ['nombre', 'disponible', 'capacidad', 'descripcion']
        labels = {
            'nombre': 'Elegir un nombre para la Clase',
            'disponible': 'Disponible',
            'capacidad': 'Capacidad máxima',
            'descripcion': 'Descripción',
        }

