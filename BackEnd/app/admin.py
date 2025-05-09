from django.contrib import admin

# Register your models here.

from .models import Usuario, Linea, Unidad, Area, TipoEstudiante, Carrera, Especialidad, Articulo,  Estudiante, Proyecto, Investigador, Evento, Herramienta , DetLinea, DetEvento, DetHerr, DetProy, DetArt, NivelEdu, NivelSNII, TipoEvento


admin.site.register(Proyecto)
admin.site.register(Investigador)
admin.site.register(Evento)
admin.site.register(Herramienta)
admin.site.register(DetLinea)
admin.site.register(DetEvento)
admin.site.register(DetHerr)
admin.site.register(DetProy)
admin.site.register(DetArt)
admin.site.register(NivelEdu)
admin.site.register(NivelSNII)
admin.site.register(Articulo)
admin.site.register(TipoEvento)
admin.site.register(Usuario)
admin.site.register(Linea)
admin.site.register(Unidad)
admin.site.register(Area)
admin.site.register(TipoEstudiante)
admin.site.register(Carrera)
admin.site.register(Especialidad)
admin.site.register(Estudiante)

