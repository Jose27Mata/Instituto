from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from .models import *

class Informe_alumnos(PDFTemplateView):
    template_name = 'informe_alumnos.html'
    def get_context_data(self, **kwargs):
        # Buscar el id del cual quiero el informe
        id_llave = self.request.GET.get('id')
        alumnos = Alumno.objects.get(id = id_llave)
        return super(Informe_alumnos, self).get_context_data(
            pagezise = 'letter',
            title = 'informe_alumnos', # Intentar concatenar nombre y apellido
            Alumno = alumnos,
            **kwargs
        )

class Informe_encargado(PDFTemplateView):
    template_name = 'informe_encargados.html'
    def get_context_data(self, **kwargs):
        # Buscar el id del cual quiero el informe
        id_llave = self.request.GET.get('id')
        encargados = Encargado.objects.get(id = id_llave)
        return super(Informe_encargado, self).get_context_data(
            pagezise = 'letter',
            title = 'Informe_encargado', # Intentar concatenar nombre y apellido
            Encargado = encargados,
            **kwargs
        )
