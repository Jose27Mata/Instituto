from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.

class Encargado(models.Model):
    # foto = models.ImageField('Fotografía')
    nombre_encargado = models.CharField(
    'Nombre completo', max_length = 40, blank = False, null = False,
    help_text =
    "Ingrese según el formato, primero nombre y luego apellidos. Ejemplo Juan José Pérez García")
    fecha_nac = models.DateField(
    'Fecha de nacimiento',  help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    dpi = models.CharField(
    'DPI (número de CUI)', max_length = 13, help_text = "Ingrese los números sin espacio")
    direccion = models.CharField(
    'Dirección de residencia', max_length = 150, blank = False, null = False)
    telefono = models.CharField(
    'Número de teléfono', max_length = 8, help_text = "Ingrese los números sin espacio")

    def Imprimirinforme (self):
        return mark_safe(u'<a href="/Informe_encargado/?id=%s"'
            'target="_blank">Imprimir Informe</a>' % self.id)
    Imprimirinforme.short_description = 'Impimir Informe'

    class Meta:
        verbose_name='Encargado'
        verbose_name_plural='Encargados'
        ordering=['nombre_encargado']

    def __str__(self):
        return self.nombre_encargado

class Alumno(models.Model):
    SEXO_CHOISES = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )
    estado = models.BooleanField(
    'Estado Activo/Inactivo', default = True,
    help_text = "Marque la casilla si el alumno está activo / Deje sin marcar si está inactivo")
    # foto = models.ImageField('Fotografía')
    codigo_personal = models.CharField(
    'Código Personal', max_length = 10, blank = False, null = False)
    nombre = models.CharField(
    'Nombre completo', max_length = 40, blank = False, null = False,
    help_text =
    "Ingrese según el formato, primero nombre y luego apellidos. Ejemplo Juan José Pérez García")
    dpi = models.CharField(
    'DPI (número de CUI)', max_length = 13, help_text = "Ingrese los números sin espacio")
    fecha_nac = models.DateField(
    'Fecha de nacimiento',  help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    sexo = models.CharField(
    'Sexo', max_length = 1, choices = SEXO_CHOISES, default = 'M')
    nombre_encargado = models.ForeignKey(Encargado, on_delete = models.CASCADE)
    direccion = models.CharField(
    'Dirección de residencia', max_length = 150, blank = False, null = False)
    telefono = models.CharField(
    'Teléfono', max_length = 8, help_text = "Ingrese los números sin espacio")

    def Imprimirinforme (self):
        return mark_safe(u'<a href="/Informe_alumnos/?id=%s"'
            'target="_blank">Imprimir Informe</a>' % self.id)
    Imprimirinforme.short_description = 'Impimir Informe'

    def getAtributo (self):
        if self.sexo == 'M':
	           return mark_safe('<span style="color: #0000FF">{0}</span>'.format('Masculino'))
        else: # en el format(self.sexo) puede ir nombre de la variable o texto puro para que aparezca
            return mark_safe('<span style="color: #ff0080">{0}</span>'.format('Femenino'))

        # Le da un nombre a la función en el informe
    getAtributo.short_description = 'Sexo'

    class Meta:
        verbose_name='Alumno'
        verbose_name_plural='Alumnos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre
