from django.db import models
from Personal.models import Profesor
from django.utils.safestring import mark_safe
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# Create your models here.

class Curso(models.Model):
    nombre = models.CharField('Nombre del Curso',
    max_length = 60, null = False)
    nota_minima = models.IntegerField('Nota Mínima',
    default = 60)
    sueldo = models.IntegerField('Pago del curso')

    class Meta:
        verbose_name='Curso'
        verbose_name_plural='Cursos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

class Asignacion(models.Model):
    nombre_curso = models.ForeignKey(
    Curso, on_delete = models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete = models.CASCADE)
    ciclo = models.CharField(
    'Ciclo de estudio', max_length = 4,
    help_text = "Ingrese el año sin espacios, ejemplo: 2020")

    def Imprimirinforme (self):
        return mark_safe(u'<a href="/Informe_curso/?id=%s"'
            'target="_blank">Imprimir Informe</a>' % self.id)
    Imprimirinforme.short_description = 'Impimir Informe'

    class Meta:
        verbose_name='Asignacion'
        verbose_name_plural='Asignaciones'
        ordering = ['nombre_curso']

    def no_repetir(self):
        for asignacion in Asignacion.objects.filter(nombre_curso = self.nombre_curso):
            if asignacion.ciclo == self.ciclo:
                if asignacion.profesor != self.profesor:
                    raise ValidationError('Este curso ya fue asignado en este ciclo')
            else:
                pass

    def clean(self, **kwargs): # funcion para el autoincremento de número de boleta
        self.no_repetir()
        super(Asignacion, self).clean()

    def __str__(self):
        return self.nombre_curso.nombre
