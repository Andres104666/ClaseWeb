from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .forms import EstudianteForm, InvestigadorForm, AreaForm, EventoForm, ProyectoForm, ArticuloForm, LineaForm
#app
from app.models import Usuario,Estudiante, Investigador,Proyecto,Area, Especialidad,Unidad, Linea, DetLinea, Articulo, Evento, DetProy, DetEvento, Proyecto, DetProy, DetEvento,DetArt, Carrera, TipoEstudiante, TipoEvento, NivelEdu, NivelSNII

from django.http.response import JsonResponse
from django.views.generic import ListView, DetailView

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serielizers import EstudianteSerializer, InvestigadorSerializer, AreaSerializer, EspecialidadesSerializer, UnidadesSerializer, ProyectosSerializer, EventosSerializer, ArticulosSerializer, AreasSerializer, LineasInvestigacionSerializer, DetProySerielizer, DetArtSerielizer, DetEventoSerializer, DetLineaSerializer, CarreraSerializer, TipoEstudianteSerializer, TipoEventoSerializer, NivelEduSerializer, NivelSNIISerializer, UsuarioSerializer


from django.views import View

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

#ENDPOINTS FAK
def get_usuarios(request):
    usuarios = Usuario.objects.all().values( 'nombre', 'email')
    return JsonResponse(list(usuarios), safe=False)

def get_areas(request):
    areas = Area.objects.all().values('nombre')
    return JsonResponse(list(areas), safe=False)

def get_niveledu(request):
    niveledu = NivelEdu.objects.all().values('descripcion')
    return JsonResponse(list(niveledu), safe=False)

def get_nivelsnii(request):
    nivelsnii = NivelSNII.objects.all().values('descripcion')
    return JsonResponse(list(nivelsnii), safe=False)

@api_view(['POST'])
def create_investigador(request):
    serializer = InvestigadorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_investigador(request, id):
    try:
        investigador = Investigador.objects.get(id=id)
        investigador.delete()
        return Response({"message": "Investigador eliminado correctamente"}, status=200)
    except Investigador.DoesNotExist:
        return Response({"error": "Investigador no encontrado"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(['GET', 'PUT'])
def investigador_detail(request, id):
    try:
        investigador = Investigador.objects.get(id=id)
    except Investigador.DoesNotExist:
        return Response({"error": "Investigador no encontrado"}, status=404)

    if request.method == 'GET':
        serializer = InvestigadorSerializer(investigador)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = InvestigadorSerializer(investigador, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)




def home(request):
    # Obtén el evento más reciente
    evento_reciente = Evento.objects.order_by('-fecha').first()

    # Obtén el artículo más reciente
    articulo_reciente = Articulo.objects.order_by('-fecha_publicacion').first()

    # Obtén el proyecto más reciente
    proyecto_reciente = Proyecto.objects.order_by('-fecha_inicio').first()

    return render(request, "home.html", {
        'evento_reciente': evento_reciente,
        'articulo_reciente': articulo_reciente,
        'proyecto_reciente': proyecto_reciente
    })

def lineas_investigacion_view(request):
    lineas = Linea.objects.all()
    for linea in lineas:
        # Agregar los investigadores asociados a cada línea
        linea.investigadores = [
            detlinea.investigador for detlinea in DetLinea.objects.filter(linea=linea)
        ]
    return render(request, 'lineas_investigacion.html', {'lineas': lineas})

    

def areas(request):
    return render(request, "areas.html")

class especialidadesListView(ListView):
    model = Especialidad
    template_name = 'especialidades.html'
    context_object_name = 'especialidades'

    def get_queryset(self):
        return Especialidad.objects.all()
    
class especialidadesDetailView(DetailView):
    model = Especialidad
    template_name = 'especialidades_det.html'
    context_object_name = 'especialidad'
    # # se le da el contexto de los investigadores que tiene la especialidad a la vista
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        especialidad = self.object  
        context['investigadores'] = Investigador.objects.filter(especialidad=especialidad)
        return context


def proyectos(request):
    area_id = request.GET.get('area')  # Obtén el área seleccionada del parámetro GET
    if area_id:
        proyectos = Proyecto.objects.filter(Area_id=area_id)  # Filtra por área
    else:
        proyectos = Proyecto.objects.all()  # Muestra todos los proyectos si no hay filtro

    areas = Area.objects.all()  # Obtén todas las áreas para el filtro

    for proyecto in proyectos:
        proyecto.investigadores = [
            DetProy.investigador for DetProy in DetProy.objects.filter(proyecto=proyecto)
        ]

    return render(request, 'proyectos.html', {'proyectos': proyectos, 'areas': areas})



def articulos(request):
    area_id = request.GET.get('area')  
    if area_id:
        articulos = Articulo.objects.filter(Area_id=area_id)  
    else:
        articulos = Articulo.objects.all()  

    areas = Area.objects.all()  

    # Agrega los investigadores asociados a cada artículo
    for articulo in articulos:
        articulo.investigadores = [
            detart.investigador for detart in DetArt.objects.filter(articulo=articulo)
        ]

    return render(request, 'articulos.html', {'articulos': articulos, 'areas': areas})






class InvestigadorListView(ListView):
    model = Investigador
    template_name = 'investigadores.html'
    context_object_name = 'investigadores'
    
    def get_queryset(self):
        
        return Investigador.objects.filter(esatus=True)

class InvestigadorDetailView(DetailView):
    model = Investigador
    template_name = 'investigadores_det.html'
    context_object_name = 'investigador'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        investigador = self.object
        
        # Asegúrate de que estos nombres coincidan con los usados en el template
        context['articulos'] = investigador.articulos.all()
        context['proyectos'] = investigador.proyectos.all()
        context['estudiantes'] = investigador.estudiante_set.all()
        context['eventos'] = investigador.eventos.all()
        
        return context

def estudiantes(request):

     query = request.GET.get('q')  
     if query:
         estudiantes = Estudiante.objects.filter(nombre__icontains=query)  
     else:
         estudiantes = Estudiante.objects.all() 
     return render(request, 'Estudiante.html', {'estudiantes': estudiantes})


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class InvestigadorViewSet(viewsets.ModelViewSet):
    queryset = Investigador.objects.all()
    serializer_class = InvestigadorSerializer

class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class EspecialidadesViewSet(viewsets.ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadesSerializer

class UnidadesViewSet(viewsets.ModelViewSet):
    queryset = Unidad.objects.all()
    serializer_class = UnidadesSerializer

class ProyectosViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectosSerializer

class EventosViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventosSerializer

class ArticulosViewSet(viewsets.ModelViewSet):
    queryset = Articulo.objects.all()
    serializer_class = ArticulosSerializer

class DetProyViewSet(viewsets.ModelViewSet):
    queryset = DetProy.objects.all()
    serializer_class = DetProySerielizer

class DetArtViewSet(viewsets.ModelViewSet):
    queryset = DetArt.objects.all()
    serializer_class = DetArtSerielizer

class AreasViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreasSerializer

class LineasInvestigacionViewSet(viewsets.ModelViewSet):
    queryset = Linea.objects.all()
    serializer_class = LineasInvestigacionSerializer

class DetEventoViewSet(viewsets.ModelViewSet):
    queryset = DetEvento.objects.all()
    serializer_class = DetEventoSerializer

class DetLineaViewSet(viewsets.ModelViewSet):
    queryset = DetLinea.objects.all()
    serializer_class = DetLineaSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    serializer_class = CarreraSerializer

class TipoEstudianteViewSet(viewsets.ModelViewSet):
    queryset = TipoEstudiante.objects.all()
    serializer_class = TipoEstudianteSerializer

class TipoEventoViewSet(viewsets.ModelViewSet):
    queryset = TipoEvento.objects.all()
    serializer_class = TipoEventoSerializer

class NivelEduViewSet(viewsets.ModelViewSet):
    queryset = NivelEdu.objects.all()
    serializer_class = NivelEduSerializer

class NivelSNIIViewSet(viewsets.ModelViewSet):
    queryset = NivelSNII.objects.all()
    serializer_class = NivelSNIISerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    






def eventos(request):
    area_id = request.GET.get('area') 
    if area_id:
        eventos = Evento.objects.filter(Area_id=area_id)  
    else:
        eventos = Evento.objects.all()  

    areas = Area.objects.all()
    return render(request, 'eventos.html', {'eventos': eventos, 'areas': areas})




class UnidadesListView(ListView):
    model = Unidad
    template_name = 'unidades.html'
    context_object_name = 'unidades'

    def get_queryset(self):
        return Unidad.objects.all()
    



def gestion_general(request):
    entidades = {
        'estudiantes': {'form': EstudianteForm, 'model': Estudiante},
        'investigadores': {'form': InvestigadorForm, 'model': Investigador},
        'areas': {'form': AreaForm, 'model': Area},
        'eventos': {'form': EventoForm, 'model': Evento},
        'proyectos': {'form': ProyectoForm, 'model': Proyecto},
        'articulos': {'form': ArticuloForm, 'model': Articulo},
        'lineas': {'form': LineaForm, 'model': Linea},
    }

    entidad_seleccionada = request.GET.get('entidad', 'estudiantes')
    entidad = entidades.get(entidad_seleccionada)

    if not entidad:
        return redirect('gestion_general')  

    FormClass = entidad['form']
    ModelClass = entidad['model']

    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_general')  
    else:
        form = FormClass()

    registros = ModelClass.objects.all()

    return render(request, 'gestion_general.html', {
        'form': form,
        'registros': registros,
        'entidad_seleccionada': entidad_seleccionada,
        'entidades': entidades.keys(),
    })


def eliminar_registro(request, entidad, pk):
    entidades = {
        'estudiantes': Estudiante,
        'investigadores': Investigador,
        'areas': Area,
        'eventos': Evento,
        'proyectos': Proyecto,
        'articulos': Articulo,
        'lineas': Linea,
    }

    ModelClass = entidades.get(entidad)
    if not ModelClass:
        return redirect('gestion_general')  

    registro = get_object_or_404(ModelClass, pk=pk)

    if request.method == 'POST':
        registro.delete()
        return redirect('gestion_general') 

    return render(request, 'confirmar_eliminacion.html', {
        'entidad': entidad,
        'registro': registro,
    })

def editar_registro(request, entidad, pk):
    entidades = {
        'estudiantes': {'form': EstudianteForm, 'model': Estudiante},
        'investigadores': {'form': InvestigadorForm, 'model': Investigador},
        'areas': {'form': AreaForm, 'model': Area},
        'eventos': {'form': EventoForm, 'model': Evento},
        'proyectos': {'form': ProyectoForm, 'model': Proyecto},
        'articulos': {'form': ArticuloForm, 'model': Articulo},
        'lineas': {'form': LineaForm, 'model': Linea},
    }

    entidad_data = entidades.get(entidad)
    if not entidad_data:
        return redirect('gestion_general')  

    ModelClass = entidad_data['model']
    FormClass = entidad_data['form']

    registro = get_object_or_404(ModelClass, pk=pk)

    if request.method == 'POST':
        form = FormClass(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('gestion_general')  
    else:
        form = FormClass(instance=registro)

    return render(request, 'editar_registro.html', {
        'form': form,
        'entidad': entidad,
        'registro': registro,
    })


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"