from django.db import models
from Informacion.models import *
from ckeditor.fields import RichTextField
# Create your models here.
GRADO_CHOISES = (
    ('1', 'Primero Básico'),
    ('2', 'Segundo Básico'),
    ('3', 'Tercero Básico')
)

PAGO_CHOISES = (
    ('Inscripción', 'Inscripción'),
    ('Mensualidad', 'Mensualidad'),
    ('Uniforme Física', 'Uniforme Física'),
    ('Playera diaria', 'Playera diaria'),
    ('Otros', 'Otros')
)
class Inscripcion(models.Model):
    papeleria_completa = models.BooleanField(
    'Papeleria completa', default = True,
    help_text = "Marque la casila si la papelería está completa")
    nombre_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    grado = models.CharField(
    'Grado', max_length = 1, choices = GRADO_CHOISES, default = '1')
    ciclo = models.CharField(
    'Ciclo de estudio', max_length = 4,
    help_text = "Ingrese el año sin espacios, ejemplo: 2020")
    archivo = models.CharField(
    'Nombre del Archivo donde se almacena los documentos', max_length = 2)
    gabeta = models.CharField(
    'Nombre de la Gabeta donde se almacenan los documentos', max_length = 2)
    folio = models.CharField(
    'Nombre del folio donde se almacenan los documentos', max_length = 2)
    detalle = models.TextField(
    'Detalle de inscripcion', max_length = 500, blank = True)
    fecha_ins = models.DateField(
    'Fecha de inscripción', help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")

    def Imprimirinforme (self):
        return mark_safe(u'<a href="/Informe_inscripcion/?id=%s"'
            'target="_blank">Imprimir Informe</a>' % self.id)
    Imprimirinforme.short_description = 'Impimir Informe'

    def Imprimirnotas (self):
        return mark_safe(u'<a href="/Informe_notas/?id=%s"'
            'target="_blank">Imprimir Notas</a>' % self.id)
    Imprimirnotas.short_description = 'Impimir Notas'

    class Meta:
        verbose_name='Inscripción'
        verbose_name_plural='Inscripciones'
        unique_together = [['nombre_alumno', 'ciclo']]
        # ordering=['']

    def __str__(self):
        return self.archivo

# class Papeleria(models.Model)
class Pagos(models.Model):
    nombre_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    fecha_pago = models.DateField(
    'Fecha de pago', help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    tipo_pago = models.CharField(
    'Tipo de pago', max_length = 20, choices = PAGO_CHOISES, default = '1')
    monto = models.DecimalField('Monto a pagar', max_digits=6, decimal_places=2,
    help_text = "Ingrese según formato. Ejemplo: 66.23, 40.00")
    detalle_pago = models.TextField(
    'Detalle de pago', blank = True)

    def mostrarMonto (self):
        quetzal = str(self.monto)
        return 'Q. %s' %(quetzal)
    mostrarMonto.short_description = 'Sueldo'

    def ImprimirinformeP (self):
        return mark_safe(u'<a href="/Informe_pagos/?id=%s"'
            'target="_blank">Imprimir Informe</a>' % self.id)
    ImprimirinformeP.short_description = 'Impimir Informe'

    class Meta:
        verbose_name='Pago'
        verbose_name_plural='Pagos'
        # ordering=['']

    def __str__(self):
        return '%s'%(self.tipo_pago)

    def MontoPago(self):
        tipo = self.tipo_pago
        if tipo=='1':
            self.monto = 70.00
        elif tipo=='2':
            self.monto = 50.00
        elif tipo=='3':
            self.monto = 80.00
        elif tipo=='4':
            self.monto = 50.00
        else:
            self.monto = self.monto

# sobreescribe el metodo del modelo para evaluar
    def save(self, **kwargs):
        self.MontoPago()
        super(Pagos, self).save()
