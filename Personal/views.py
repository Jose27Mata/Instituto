from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from .models import Profesor
from .models import Otros
# Create your views here.
class Informe_profesor(PDFTemplateView):
    template_name = 'Informe_profesor.html'
    def get_context_data(self, **kwargs):
        # Buscar el id del cual quiero el informe
        id_llave = self.request.GET.get('id')
        profesores = Profesor.objects.get(id = id_llave)
        return super(Informe_profesor, self).get_context_data(
            pagezise = 'letter',
            title = 'Informe_profesor', # Intentar concatenar nombre y apellido
            Profesor = profesores,
            **kwargs
        )

class Informe_otro(PDFTemplateView):
    template_name = 'informe_otros.html'
    def get_context_data(self, **kwargs):
        # Buscar el id del cual quiero el informe
        id_llave = self.request.GET.get('id')
        otros = Otros.objects.get(id = id_llave)
        return super(Informe_otro, self).get_context_data(
            pagezise = 'letter',
            title = 'informe_otro', # Intentar concatenar nombre y apellido
            Otro = otros,
            **kwargs
        )
