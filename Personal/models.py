from django.db import models
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
# Create your models here.

PUESTO_CHOISES = (
    ('Director', 'Director'),
    ('Secretaria', 'Secretaria'),
    ('Conserje', 'Conserje')
)

class Profesor(models.Model):
    estado = models.BooleanField(
    'Estado Activo/Inactivo', default = True)
    codigo = models.IntegerField(
    'Código del Profesor')
    nombre = models.CharField(
    'Nombre completo', max_length = 40, blank = False, null = False,
    help_text =
    "Ingrese según el formato, primero nombre y luego apellidos. Ejemplo Juan José Pérez García")
    fecha_nac = models.DateField(
    'Fecha de nacimiento', help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    dpi = models.CharField(
    'DPI (número de CUI)', max_length = 13, help_text = "Ingrese los números sin espacio")
    direccion = models.CharField(
    'Dirección de residencia', max_length = 40, blank = False, null = False)
    telefono = models.CharField(
    'Telefono', max_length = 8, help_text = "Ingrese los números sin espacio")

    def Imprimirinforme (self):
        return mark_safe(u'<a href="/Informe_profesor/?id=%s"'
            'target="_blank">Imprimir Informe</a>' % self.id)
    Imprimirinforme.short_description = 'Impimir Informe'

    def Sueldo (self):
        sueldo = 0
        from Curso.models import Asignacion
        hoy = datetime.now()
        for asignacion in Asignacion.objects.filter(profesor = self.id, ciclo = hoy.year):
            sueldo = sueldo + asignacion.nombre_curso.sueldo
        return 'Q. %s' % (sueldo)

    class Meta:
        verbose_name='Profesor'
        verbose_name_plural='Profesores'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Otros(models.Model):
    estado = models.BooleanField(
    'Estado Activo/Inactivo', default = True)
    puesto = models.CharField(
    'Puesto del trabajador', max_length = 12, choices = PUESTO_CHOISES, default = '1')
    nombre = models.CharField(
    'Nombre completo', max_length = 40, blank = False, null = False,
    help_text =
    "Ingrese según el formato, primero nombre y luego apellidos. Ejemplo Juan José Pérez García")
    dpi = models.CharField(
    'DPI (número de CUI)', max_length = 13, help_text = "Ingrese los números sin espacio")
    fecha_nac = models.DateField(
    'Fecha de nacimiento', help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    direccion = models.CharField(
    'Dirección de residencia', max_length = 40, blank = False, null = False)
    telefono = models.CharField(
    'Telefono', max_length = 8, help_text = "Ingrese los números sin espacio")
    sueldo = models.DecimalField(max_digits=6, decimal_places=2)

    def mostrarMonto (self):
        quetzal = str(self.sueldo)
        return 'Q. %s' %(quetzal)
    mostrarMonto.short_description = 'Sueldo'

    def Imprimirinforme (self):
        return mark_safe(u'<a href="/Informe_otro/?id=%s"'
            'target="_blank">Imprimir Informe</a>' % self.id)
    Imprimirinforme.short_description = 'Impimir Informe'

    class Meta:
        verbose_name='Otro Puestos'
        verbose_name_plural='Otros Puestos'
        ordering = ['nombre']
    def __str__(self):
        return self.nombre
