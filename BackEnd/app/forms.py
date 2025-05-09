from django import forms
from .models import Estudiante, Investigador, Area, Evento, Proyecto, Articulo, Linea

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'  

class InvestigadorForm(forms.ModelForm):
    class Meta:
        model = Investigador
        fields = '__all__'

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = '__all__'

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'

class ArticuloForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = '__all__'

class LineaForm(forms.ModelForm):
    class Meta:
        model = Linea
        fields = '__all__'