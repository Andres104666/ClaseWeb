from rest_framework import serializers
from .models import Usuario, DetLinea, DetEvento, DetArt ,DetProy, Estudiante, Investigador, Especialidad, Unidad, Proyecto, Evento, Articulo, Area, Linea, Carrera, TipoEstudiante, TipoEvento, NivelEdu, NivelSNII  # Importa tu modelo

class DetHerrSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetProy 
        fields = '__all__'  

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrera
        fields = '__all__'

class TipoEstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEstudiante

        fields = '__all__' 

class TipoEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoEvento
        fields = '__all__' 

class NivelEduSerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelEdu
        fields = '__all__'  

class NivelSNIISerializer(serializers.ModelSerializer):
    class Meta:
        model = NivelSNII
        fields = '__all__'  

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'  
class InvestigadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investigador
        fields = '__all__'  

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'

class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad

        fields = '__all__'  

class UnidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unidad
        fields = '__all__'  

class ProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'  

class EventosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class ArticulosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo

        fields = '__all__'

class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'  

class LineasInvestigacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linea
        fields = '__all__'  

class DetProySerielizer(serializers.ModelSerializer):
    class Meta:
        model = DetProy 
        fields = '__all__'  
    
class DetArtSerielizer(serializers.ModelSerializer):
    class Meta:
        model = DetArt 
        fields = '__all__'  

class DetEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetEvento 
        fields = '__all__'  

class DetLineaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetLinea 
        fields = '__all__'  

  



 
