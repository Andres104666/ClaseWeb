from django.urls import path,include

from .views import SignUpView, InvestigadorListView, InvestigadorDetailView, especialidadesDetailView, especialidadesListView, UnidadesListView  
from . import views

from rest_framework.routers import DefaultRouter
from .views import  EstudianteViewSet, InvestigadorViewSet, TipoEventoViewSet, EspecialidadesViewSet, UnidadesViewSet, ProyectosViewSet, EventosViewSet, ArticulosViewSet, AreasViewSet, LineasInvestigacionViewSet, UsuarioViewSet, DetProyViewSet, DetEventoViewSet, DetArtViewSet, DetLineaViewSet, CarreraViewSet, TipoEstudianteViewSet, NivelEduViewSet, NivelSNIIViewSet
from .views import get_areas, get_usuarios, get_niveledu,  get_nivelsnii, delete_investigador


router = DefaultRouter()
router.register(r'Estudiante', EstudianteViewSet )
router.register(r'Investigador', InvestigadorViewSet )
router.register(r'Especialidad', EspecialidadesViewSet )
router.register(r'Unidad', UnidadesViewSet )
router.register(r'Proyecto', ProyectosViewSet )
router.register(r'Evento', EventosViewSet )
router.register(r'Articulo', ArticulosViewSet )
router.register(r'Areas', AreasViewSet)
router.register(r'LineasInvestigacion', LineasInvestigacionViewSet )
router.register(r'DetProy', DetProyViewSet )
router.register(r'DetEvento', DetEventoViewSet )
router.register(r'DetArt', DetArtViewSet )
router.register(r'DetLinea', DetLineaViewSet )
router.register(r'Carrera', CarreraViewSet )
router.register(r'TipoEstudiante', TipoEstudianteViewSet )
router.register(r'NivelEdu', NivelEduViewSet )
router.register(r'NivelSNII', NivelSNIIViewSet )
router.register(r'Usuario', UsuarioViewSet )
router.register(r'TipoEvento', TipoEventoViewSet )



#endpoints

path('api/usuarios/', get_usuarios, name='get_usuarios'),
path('api/areas/', get_areas, name='get_areas'),
path('api/niveledu/', get_niveledu, name='get_niveledu'),
path('api/nievlsnii/', get_nivelsnii, name='get_nivelsnii'),
path('api/Investigador/<int:id>/', delete_investigador, name='delete_investigador'),



urlpatterns = [

    path('', include(router.urls)),

    path("home/", views.home, name="home"),


    path("lineas_investigacion/", views.lineas_investigacion_view, name="lineas_investigacion"),


    path("areas/", views.areas, name="areas"),

    path("especialidades/", especialidadesListView.as_view(), name="especialidades"),
    path("especialidades_det/<int:pk>/", especialidadesDetailView.as_view(), name="especialidad_det"),

    path("proyectos/", views.proyectos, name="proyectos"),


    path('investigadores/', InvestigadorListView.as_view(), name='investigadores'),
    path('investigadores_det/<int:pk>/', InvestigadorDetailView.as_view(), name='investigadores_det'),


    path("estudiantes/", views.estudiantes, name="estudiantes"),



    

    path("eventos/", views.eventos, name="eventos"),


    path("articulos/", views.articulos, name="articulos"),


    path("unidades/", UnidadesListView.as_view(), name="unidades"),
    path('gestion/', views.gestion_general, name='gestion_general'),
    path('gestion/<str:entidad>/editar/<int:pk>/', views.editar_registro, name='editar_registro'),
    path('gestion/<str:entidad>/eliminar/<int:pk>/', views.eliminar_registro, name='eliminar_registro'),


    path("signup/", SignUpView.as_view(), name="signup"),
]
