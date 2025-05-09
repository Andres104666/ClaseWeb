from django.db import models



class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    esatus = models.BooleanField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nombre} {self.email} {self.esatus} {self.password}'


class Linea(models.Model):
    nombre = models.CharField(max_length=100)
    esatus = models.BooleanField()


    def __str__(self):
        return f'{self.nombre} {self.esatus}'


class Unidad(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    esatus = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} {self.ubicacion} {self.esatus}'


class Area(models.Model):
    nombre = models.CharField(max_length=100)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    esatus = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} {self.unidad} {self.esatus}'


class TipoEstudiante(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'


class Carrera(models.Model):
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.descripcion}'


class Especialidad(models.Model):
    descripcion = models.CharField(max_length=100) 
    esatus = models.BooleanField()

    def __str__(self):
        return f'{self.descripcion}'


class NivelEdu(models.Model):
    descripcion = models.CharField(max_length=50)
    esatus = models.BooleanField()

    def __str__(self):
        return f'{self.descripcion}  {self.esatus}'


class NivelSNII(models.Model):
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.descripcion}'


class TipoEvento(models.Model):
    descripcion = models.CharField(max_length=100)
    esatus = models.BooleanField()
    
    def __str__(self):
        return f'{self.descripcion} {self.esatus}'

class Articulo(models.Model):
    ESTATUS_OPCIONES = [
        ('planeacion', 'En planeación'),
        ('proceso', 'En proceso'),
        ('terminado', 'Terminado'),
    ]


    titulo = models.CharField(max_length=255)
    fecha_publicacion = models.DateField()
    enlace = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=100)
    Area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.titulo} '


class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255, default='')
    fecha = models.DateField()
    tipo_evento = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)
    ubicacion = models.CharField(max_length=255, default='')
    organizador = models.CharField(max_length=100, default='')

    def __str__(self):
        return f'{self.nombre} '


class Herramienta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    esatus = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} {self.descripcion} {self.esatus}'


class Proyecto(models.Model):
    ESTATUS_OPCIONES = [
        ('planeacion', 'En planeación'),
        ('proceso', 'En proceso'),
        ('terminado', 'Terminado'),
    ]

    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255, null=True, blank=True)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    esatus = models.CharField(max_length=20, choices=ESTATUS_OPCIONES, default='planeacion')
    herramientas = models.ManyToManyField(Herramienta, through='DetHerr')
    Area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.nombre} '


class Investigador(models.Model):
    nombre = models.CharField(max_length=255)
    tel = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    nivel_edu = models.ForeignKey(NivelEdu, on_delete=models.CASCADE)
    snii = models.ForeignKey(NivelSNII, on_delete=models.CASCADE)
    esatus = models.BooleanField()
    lineas = models.ManyToManyField(Linea, through='DetLinea')
    articulos = models.ManyToManyField(Articulo, through='DetArt',blank=True)
    eventos = models.ManyToManyField(Evento, through='DetEvento', blank=True)
    proyectos = models.ManyToManyField(Proyecto, through='DetProy', blank=True)
    

    def __str__(self):
        return f'{self.nombre}'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    tel = models.CharField(max_length=25)
    email = models.CharField(max_length=255)
    tipo = models.ForeignKey(TipoEstudiante, on_delete=models.CASCADE)
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE)
    investigador = models.ForeignKey(Investigador, on_delete=models.CASCADE)
    esatus = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} {self.carrera} {self.tipo} {self.investigador} {self.esatus} {self.email} {self.tel}'



class DetLinea(models.Model):
    investigador = models.ForeignKey(Investigador, on_delete=models.CASCADE)
    linea = models.ForeignKey(Linea, on_delete=models.CASCADE)


    class Meta:
        unique_together = ('investigador', 'linea')

    def __str__(self):
        return f'{self.investigador} {self.linea}'


class DetArt(models.Model):
    investigador = models.ForeignKey(Investigador, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('investigador', 'articulo')

    def __str__(self):
        return f'{self.investigador} {self.articulo}'


class DetEvento(models.Model):
    investigador = models.ForeignKey(Investigador, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('investigador', 'evento')

    def __str__(self):
        return f'{self.investigador} {self.evento}'

class DetProy(models.Model):
    investigador = models.ForeignKey(Investigador, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    

    class Meta:
        unique_together = ('investigador', 'proyecto' )

    def __str__(self):
        return f'{self.investigador} {self.proyecto}'


class DetHerr(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('proyecto', 'herramienta')

    def __str__(self):
        return f'{self.proyecto} {self.herramienta}'