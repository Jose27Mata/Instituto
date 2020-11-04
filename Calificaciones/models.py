from django.db import models
from ckeditor.fields import RichTextField
from Informacion.models import *
from Curso.models import Curso

# Create your models here.
class Notas(models.Model):
    nombre_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    fecha = models.DateField('Fecha',
    help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    bimestre = models.IntegerField(
    'Bimestre', blank = False, help_text =
    "Ingrese el bimestre correspondiente a las notas. Ejemplo: 1, 2, 3, 4")
    curso = models.ForeignKey(Curso, on_delete = models.CASCADE)
    nota = models.IntegerField('Nota',
    blank = False,
    help_text = "Ingrese el numero sin espacios, ejemplos: 04, 32, 54, 89")

    class Meta:
        verbose_name='Nota'
        verbose_name_plural='Notas'
        ordering = ['nombre_alumno']

    def __str__(self):
        return '%s %s' %(self.nombre_alumno, self.bimestre)

class Matematicas(models.Model):
    fecha = models.DateField('Fecha',
    help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    ciclo = models.CharField(
    'Ciclo de estudio', max_length = 4,
    help_text = "Ingrese el año sin espacios, ejemplo: 2020")
    bimestre = models.IntegerField(
    'Bimestre', blank = False, help_text =
    "Ingrese el bimestre correspondiente a las notas. Ejemplo: 1, 2, 3, 4")
    nombre_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    nota_mate = models.IntegerField('Nota Matemáticas',
    blank = False,
    help_text = "Ingrese el numero sin espacios, ejemplos: 04, 32, 54, 89")
    detalle = models.TextField('Detalle de inscripción', max_length = 500, blank = True)

    # NOTA MATE
    def getNota_Mate (self):
        if self.nota_mate >= 60:
	           return mark_safe('<span style="color: #3b83bd">{0}</span>'.format(self.nota_mate))
        else: # en el format(self.sexo) puede ir nombre de la variable o texto puro para que aparezca
            return mark_safe('<span style="color: #FF0000">{0}</span>'.format(self.nota_mate))
    getNota_Mate.short_description = 'Nota Matemáticas'

    class Meta:
        verbose_name='Matemáticas'
        verbose_name_plural='Matemáticas'
        ordering = ['nombre_alumno']

    def __str__(self):
        return '%s %s' %(self.bimestre, self.ciclo)


class Cultura(models.Model):
    fecha = models.DateField('Fecha',
    help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    ciclo = models.CharField(
    'Ciclo de estudio', max_length = 4,
    help_text = "Ingrese el año sin espacios, ejemplo: 2020")
    bimestre = models.IntegerField(
    'Bimestre', blank = False, help_text =
    "Ingrese el bimestre correspondiente a las notas. Ejemplo: 1, 2, 3, 4")
    nombre_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    nota_cultura = models.IntegerField('Nota Cultura e Idioma Maya',
    blank = False,
    help_text = "Ingrese el numero sin espacios, ejemplos: 04, 32, 54, 89")
    detalle = models.TextField('Detalle de inscripción', max_length = 500, blank = True)

    # NOTA CULTURA
    def getNota_Cultura (self):
        if self.nota_cultura >= 60:
	           return mark_safe('<span style="color: #3b83bd">{0}</span>'.format(self.nota_cultura))
        else: # en el format(self.sexo) puede ir nombre de la variable o texto puro para que aparezca
            return mark_safe('<span style="color: #FF0000">{0}</span>'.format(self.nota_cultura))
    getNota_Cultura.short_description = 'Nota Cultura e Idioma Maya'

    class Meta:
        verbose_name='Cultura e Idioma Maya'
        verbose_name_plural='Cultura e Idioma Maya'
        ordering = ['nombre_alumno']

    def __str__(self):
        return '%s %s' %(self.bimestre, self.ciclo)


class Español(models.Model):
    fecha = models.DateField('Fecha',
    help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    ciclo = models.CharField(
    'Ciclo de estudio', max_length = 4,
    help_text = "Ingrese el año sin espacios, ejemplo: 2020")
    bimestre = models.IntegerField(
    'Bimestre', blank = False, help_text =
    "Ingrese el bimestre correspondiente a las notas. Ejemplo: 1, 2, 3, 4")
    nombre_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    nota_español = models.IntegerField('Nota Comunicación y Lenguaje, Idioma Español',
    blank = False,
    help_text = "Ingrese el numero sin espacios, ejemplos: 04, 32, 54, 89")
    detalle = models.TextField('Detalle de inscripción', max_length = 500, blank = True)

    # NOTA ESPAÑOL
    def getNota_Español (self):
        if self.nota_español >= 60:
	           return mark_safe('<span style="color: #3b83bd">{0}</span>'.format(self.nota_español))
        else: # en el format(self.sexo) puede ir nombre de la variable o texto puro para que aparezca
            return mark_safe('<span style="color: #FF0000">{0}</span>'.format(self.nota_español))
    getNota_Español.short_description = 'Nota Comunicación y Lenguaje, Idioma Español'

    class Meta:
        verbose_name='Comunicación y Lenguaje, Idioma Español'
        verbose_name_plural='Comunicación y Lenguaje, Idioma Español'
        ordering = ['nombre_alumno']

    def __str__(self):
        return '%s %s' %(self.bimestre, self.ciclo)


class Ingles(models.Model):
    fecha = models.DateField('Fecha',
    help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    ciclo = models.CharField(
    'Ciclo de estudio', max_length = 4,
    help_text = "Ingrese el año sin espacios, ejemplo: 2020")
    bimestre = models.IntegerField(
    'Bimestre', blank = False, help_text =
    "Ingrese el bimestre correspondiente a las notas. Ejemplo: 1, 2, 3, 4")
    nombre_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    nota_ingles = models.IntegerField('Nota Comunicación y Lenguaje, Idioma Extranjero',
    blank = False,
    help_text = "Ingrese el numero sin espacios, ejemplos: 04, 32, 54, 89")
    detalle = models.TextField('Detalle de inscripción', max_length = 500, blank = True)

    # NOTA INGELS
    def getNota_Ingles (self):
        if self.nota_ingles >= 60:
	           return mark_safe('<span style="color: #3b83bd">{0}</span>'.format(self.nota_ingles))
        else: # en el format(self.sexo) puede ir nombre de la variable o texto puro para que aparezca
            return mark_safe('<span style="color: #FF0000">{0}</span>'.format(self.nota_ingles))
    getNota_Ingles.short_description = 'Nota Comunicación y Lenguaje, Idioma Extranjero'

    class Meta:
        verbose_name='Comunicación y Lenguaje, Idioma Extranjero'
        verbose_name_plural='Comunicación y Lenguaje, Idioma Extranjero'
        ordering = ['nombre_alumno']

    def __str__(self):
        return '%s %s' %(self.bimestre, self.ciclo)


class Artistica(models.Model):
    fecha = models.DateField('Fecha',
    help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    ciclo = models.CharField(
    'Ciclo de estudio', max_length = 4,
    help_text = "Ingrese el año sin espacios, ejemplo: 2020")
    bimestre = models.IntegerField(
    'Bimestre', blank = False, help_text =
    "Ingrese el bimestre correspondiente a las notas. Ejemplo: 1, 2, 3, 4")
    nombre_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    nota_artistica = models.IntegerField('Nota Educación y Expresión Artística',
    blank = False,
    help_text = "Ingrese el numero sin espacios, ejemplos: 04, 32, 54, 89")
    detalle = models.TextField('Detalle de inscripción', max_length = 500, blank = True)

    # NOTA ARTISTICA
    def getNota_Artistica (self):
        if self.nota_artistica >= 60:
	           return mark_safe('<span style="color: #3b83bd">{0}</span>'.format(self.nota_artistica))
        else: # en el format(self.sexo) puede ir nombre de la variable o texto puro para que aparezca
            return mark_safe('<span style="color: #FF0000">{0}</span>'.format(self.nota_artistica))
    getNota_Artistica.short_description = 'Nota Educación y Expresión Artística'

    class Meta:
        verbose_name='Educación y Expresión Artística'
        verbose_name_plural='Educación y Expresión Artística'
        ordering = ['nombre_alumno']

    def __str__(self):
        return '%s %s' %(self.bimestre, self.ciclo)


class Productividad(models.Model):
    fecha = models.DateField('Fecha',
    help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    ciclo = models.CharField(
    'Ciclo de estudio', max_length = 4,
    help_text = "Ingrese el año sin espacios, ejemplo: 2020")
    bimestre = models.IntegerField(
    'Bimestre', blank = False, help_text =
    "Ingrese el bimestre correspondiente a las notas. Ejemplo: 1, 2, 3, 4")
    nombre_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    nota_productividad = models.IntegerField('Nota Emprendimiento para la Productividad',
    blank = False,
    help_text = "Ingrese el numero sin espacios, ejemplos: 04, 32, 54, 89")
    detalle = models.TextField('Detalle de inscripción', max_length = 500, blank = True)

    # NOTA PRODUCTIVADA
    def getNota_Productividad (self):
        if self.nota_productividad >= 60:
	           return mark_safe('<span style="color: #3b83bd">{0}</span>'.format(self.nota_productividad))
        else: # en el format(self.sexo) puede ir nombre de la variable o texto puro para que aparezca
            return mark_safe('<span style="color: #FF0000">{0}</span>'.format(self.nota_productividad))
    getNota_Productividad.short_description = 'Nota Emprendimiento para la Productividad'

    class Meta:
        verbose_name='Emprendimiento para la Productividad'
        verbose_name_plural='Emprendimiento para la Productividad'
        ordering = ['nombre_alumno']

    def __str__(self):
        return '%s %s' %(self.bimestre, self.ciclo)


class Tecnologia(models.Model):
    fecha = models.DateField('Fecha',
    help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    ciclo = models.CharField(
    'Ciclo de estudio', max_length = 4,
    help_text = "Ingrese el año sin espacios, ejemplo: 2020")
    bimestre = models.IntegerField(
    'Bimestre', blank = False, help_text =
    "Ingrese el bimestre correspondiente a las notas. Ejemplo: 1, 2, 3, 4")
    nombre_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    nota_tecnologia = models.IntegerField('Nota Tecnologías del Aprendizaje y la Comunicación',
    blank = False,
    help_text = "Ingrese el numero sin espacios, ejemplos: 04, 32, 54, 89")
    detalle = models.TextField('Detalle de inscripción', max_length = 500, blank = True)

    # NOTA TECNLOGIA
    def getNota_Tecnologia (self):
        if self.nota_tecnologia >= 60:
	           return mark_safe('<span style="color: #3b83bd">{0}</span>'.format(self.nota_tecnologia))
        else: # en el format(self.sexo) puede ir nombre de la variable o texto puro para que aparezca
            return mark_safe('<span style="color: #FF0000">{0}</span>'.format(self.nota_tecnologia))
    getNota_Tecnologia.short_description = 'Nota Tecnologías del Aprendizaje y la Comunicación'

    class Meta:
        verbose_name='Tecnologías del Aprendizaje y la Comunicación'
        verbose_name_plural='Tecnologías del Aprendizaje y la Comunicación'
        ordering = ['nombre_alumno']

    def __str__(self):
        return '%s %s' %(self.bimestre, self.ciclo)


class Fisica(models.Model):
    fecha = models.DateField('Fecha',
    help_text = "Ingrese según el formato. Ejemplo: 13/03/2005")
    ciclo = models.CharField(
    'Ciclo de estudio', max_length = 4,
    help_text = "Ingrese el año sin espacios, ejemplo: 2020")
    bimestre = models.IntegerField(
    'Bimestre', blank = False, help_text =
    "Ingrese el bimestre correspondiente a las notas. Ejemplo: 1, 2, 3, 4")
    nombre_alumno = models.ForeignKey(Alumno, on_delete = models.CASCADE)
    nota_fisica = models.IntegerField('Nota Educación Física',
    blank = False,
    help_text = "Ingrese el numero sin espacios, ejemplos: 04, 32, 54, 89")
    comentario = RichTextField('Comentario sobre el bimestre')
    detalle = models.TextField('Detalle de inscripción', max_length = 500, blank = True)

    # NOTA FISICA
    def getNota_Fisica (self):
        if self.nota_fisica >= 60:
	           return mark_safe('<span style="color: #3b83bd">{0}</span>'.format(self.nota_fisica))
        else: # en el format(self.sexo) puede ir nombre de la variable o texto puro para que aparezca
            return mark_safe('<span style="color: #FF0000">{0}</span>'.format(self.nota_fisica))
    getNota_Fisica.short_description = 'Nota Educación Física'

    class Meta:
        verbose_name='Educación Física'
        verbose_name_plural='Educación Física'
        ordering = ['nombre_alumno']

    def __str__(self):
        return '%s %s' %(self.bimestre, self.ciclo)
