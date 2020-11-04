from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from .models import *
# Create your views here.

class Informe_curso(PDFTemplateView):
    template_name = 'Informe_curso.html'
    def get_context_data(self, **kwargs):
        # Buscar el id del cual quiero el informe
        id_llave = self.request.GET.get('id')
        asignaciones = Asignacion.objects.get(id = id_llave)
        return super(Informe_curso, self).get_context_data(
            pagezise = 'letter',
            title = 'Informe_curso', # Intentar concatenar nombre y apellido
            Asignacion = asignaciones,
            **kwargs
        )
