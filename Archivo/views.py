from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from .models import Inscripcion
from .models import Pagos
from Calificaciones.models import *
# Create your views here.

class Informe_inscripcion(PDFTemplateView):
    template_name = 'informe_inscripcion.html'
    def get_context_data(self, **kwargs):
        # Buscar el id del cual quiero el informe
        id_llave = self.request.GET.get('id')
        inscripcion = Inscripcion.objects.get(id = id_llave)
        return super(Informe_inscripcion, self).get_context_data(
            pagezise = 'letter',
            title = 'inscripcion_alumno', # Intentar concatenar nombre y apellido
            Alumno = inscripcion,
            **kwargs
        )

class Informe_pagos(PDFTemplateView):
    template_name = 'informe_pagos.html'
    def get_context_data(self, **kwargs):
        # Buscar el id del cual quiero el informe
        id_llave = self.request.GET.get('id')
        pagos = Pagos.objects.get(id = id_llave)
        return super(Informe_pagos, self).get_context_data(
            pagezise = 'letter',
            title = 'informe_pagos', # Intentar concatenar nombre y apellido
            Pagos = pagos,
            **kwargs
        )

class Informe_notas(PDFTemplateView):
    template_name = 'informe_notas.html'
    def get_context_data(self, **kwargs):
        # Buscar el id del cual quiero el informe
        id_llave = self.request.GET.get('id')
        inscripcion = Inscripcion.objects.get(id = id_llave)
        alumno = inscripcion.nombre_alumno
        notas = []
        bimestre1 = {} # promedios
        bimestre2 = {}
        bimestre3 = {}
        bimestre4 = {}
        promedio1 = 0 # los promedios bimestrales
        promedio2 = 0
        promedio3 = 0
        promedio4 = 0
        mate = 0 # variable para sumar los 240
        cultura = 0
        español = 0
        ingles = 0
        artistica = 0
        productividad = 0
        tecnologia = 0
        fisica = 0
        # ------------------------------------------------------
        # bim 1 ------------------------------------------------
        bimestre1['bimestre'] = 1
        if(Matematicas.objects.filter(nombre_alumno = alumno,
        bimestre = 1).exists()):
            m1 = Matematicas.objects.filter(nombre_alumno = alumno,
            bimestre = 1).get()
            promedio1 = promedio1+m1.nota_mate # promedio bimestral
            bimestre1 ['Matematicas'] = m1.nota_mate
            mate = mate + m1.nota_mate # variable para sumar los 240
        else:
            m1 = 'NNI'
            bimestre1 ['Matematicas'] = m1

        if(Cultura.objects.filter(nombre_alumno = alumno,
        bimestre = 1).exists()):
            c1 = Cultura.objects.filter(nombre_alumno = alumno,
            bimestre = 1).get()
            promedio1 = promedio1+c1.nota_cultura
            bimestre1 ['Cultura'] = c1.nota_cultura
            cultura = cultura + c1.nota_cultura # variable para sumar los 240
        else:
            c1 = 'NNI'
            bimestre1 ['Cultura'] = c1

        if(Español.objects.filter(nombre_alumno = alumno,
        bimestre = 1).exists()):
            e1 = Español.objects.filter(nombre_alumno = alumno,
            bimestre = 1).get()
            promedio1 = promedio1+e1.nota_español
            bimestre1 ['Español'] = e1.nota_español
            español = español + e1.nota_español # variable para sumar 240
        else:
            e1 = 'NNI'
            bimestre1 ['Español'] = e1

        if(Ingles.objects.filter(nombre_alumno = alumno,
        bimestre = 1).exists()):
            i1 = Ingles.objects.filter(nombre_alumno = alumno,
            bimestre = 1).get()
            promedio1 = promedio1+i1.nota_ingles
            bimestre1 ['Ingles'] = i1.nota_ingles
            ingles = ingles + i1.nota_ingles # variable para sumar 240
        else:
            i1 = 'NNI'
            bimestre1 ['Ingles'] = i1

        if(Artistica.objects.filter(nombre_alumno = alumno,
        bimestre = 1).exists()):
            a1 = Artistica.objects.filter(nombre_alumno = alumno,
            bimestre = 1).get()
            promedio1 = promedio1+a1.nota_artistica
            bimestre1 ['Artistica'] = a1.nota_artistica
            artistica = artistica + a1.nota_artistica # variable para sumar 240
        else:
            a1 = 'NNI'
            bimestre1 ['Artistica'] = a1

        if(Productividad.objects.filter(nombre_alumno = alumno,
        bimestre = 1).exists()):
            p1 = Productividad.objects.filter(nombre_alumno = alumno,
            bimestre = 1).get()
            promedio1 = promedio1+p1.nota_productividad
            bimestre1 ['Productividad'] = p1.nota_productividad
            productividad = productividad + p1.nota_productividad # variable para sumar 240
        else:
            p1 = 'NNI'
            bimestre1 ['Productividad'] = p1

        if(Tecnologia.objects.filter(nombre_alumno = alumno,
        bimestre = 1).exists()):
            t1 = Tecnologia.objects.filter(nombre_alumno = alumno,
            bimestre = 1).get()
            promedio1 = promedio1+t1.nota_tecnologia
            bimestre1 ['Tecnologia'] = t1.nota_tecnologia
            tecnologia = tecnologia + t1.nota_tecnologia # variable para sumar 240
        else:
            t1 = 'NNI'
            bimestre1 ['Tecnologia'] = t1

        if(Fisica.objects.filter(nombre_alumno = alumno,
        bimestre = 1).exists()):
            f1 = Fisica.objects.filter(nombre_alumno = alumno,
            bimestre = 1).get()
            promedio1 = promedio1+f1.nota_fisica # promedio bimestral
            bimestre1 ['Fisica'] = f1.nota_fisica
            fisica = fisica + f1.nota_fisica # variable para sumar 240
        else:
            f1 = 'NNI'
            bimestre1 ['Fisica'] = f1

        bimestre1 ['Promedio'] = promedio1/8
        notas.append(bimestre1)
        # ------------------------------------------------------
        # bim 2 ------------------------------------------------
        bimestre2 = {}
        bimestre2['bimestre'] = 2
        if(Matematicas.objects.filter(nombre_alumno = alumno,
        bimestre = 2).exists()):
            m2 = Matematicas.objects.filter(nombre_alumno = alumno,
            bimestre = 2).get()
            promedio2 = promedio2+m2.nota_mate # promedio bimestral
            bimestre2 ['Matematicas'] = m2.nota_mate
            mate = mate + m2.nota_mate
        else:
            m2 = 'NNI'
            bimestre2 ['Matematicas'] = m2

        if(Cultura.objects.filter(nombre_alumno = alumno,
        bimestre = 2).exists()):
            c2 = Cultura.objects.filter(nombre_alumno = alumno,
            bimestre = 2).get()
            promedio2 = promedio2+c2.nota_cultura # promedio bimestral
            bimestre2 ['Cultura'] = c2.nota_cultura
            cultura = cultura + c2.nota_cultura # variable para sumar los 240
        else:
            c2 = 'NNI'
            bimestre2 ['Cultura'] = c2

        if(Español.objects.filter(nombre_alumno = alumno,
        bimestre = 2).exists()):
            e2 = Español.objects.filter(nombre_alumno = alumno,
            bimestre = 2).get()
            promedio2 = promedio2+e2.nota_español # promedio bimestral
            bimestre2 ['Español'] = e2.nota_español
            español = español + e2.nota_español # variable para sumar 240
        else:
            e2 = 'NNI'
            bimestre2 ['Español'] = e2

        if(Ingles.objects.filter(nombre_alumno = alumno,
        bimestre = 2).exists()):
            i2 = Ingles.objects.filter(nombre_alumno = alumno,
            bimestre = 2).get()
            promedio2 = promedio2+i2.nota_ingles # promedio bimestral
            bimestre2 ['Ingles'] = i2.nota_ingles
            ingles = ingles + i2.nota_ingles # variable para sumar 240
        else:
            i2 = 'NNI'
            bimestre2 ['Ingles'] = i2

        if(Artistica.objects.filter(nombre_alumno = alumno,
        bimestre = 2).exists()):
            a2 = Artistica.objects.filter(nombre_alumno = alumno,
            bimestre = 2).get()
            promedio2 = promedio2+a2.nota_artistica # promedio bimestral
            bimestre2 ['Artistica'] = a2.nota_artistica
            artistica = artistica + a2.nota_artistica # variable para sumar 240
        else:
            a2 = 'NNI'
            bimestre2 ['Artistica'] = a2

        if(Productividad.objects.filter(nombre_alumno = alumno,
        bimestre = 2).exists()):
            p2 = Productividad.objects.filter(nombre_alumno = alumno,
            bimestre = 2).get()
            promedio2 = promedio2+p2.nota_productividad # promedio bimestral
            bimestre2 ['Productividad'] = p2.nota_productividad
            productividad = productividad + p2.nota_productividad # variable para sumar 240
        else:
            p2 = 'NNI'
            bimestre2 ['Productividad'] = p2

        if(Tecnologia.objects.filter(nombre_alumno = alumno,
        bimestre = 2).exists()):
            t2 = Tecnologia.objects.filter(nombre_alumno = alumno,
            bimestre = 2).get()
            promedio2 = promedio2+t2.nota_tecnologia # promedio bimestral
            bimestre2 ['Tecnologia'] = t2.nota_tecnologia
            tecnologia = tecnologia + t2.nota_tecnologia # variable para sumar 240
        else:
            t2 = 'NNI'
            bimestre2 ['Tecnologia'] = t2

        if(Fisica.objects.filter(nombre_alumno = alumno,
        bimestre = 2).exists()):
            f2 = Fisica.objects.filter(nombre_alumno = alumno,
            bimestre = 2).get()
            promedio2 = promedio2+f2.nota_fisica # promedio bimestral
            bimestre2 ['Fisica'] = f2.nota_fisica
            fisica = fisica + f2.nota_fisica # variable para sumar 240
        else:
            f2 = 'NNI'
            bimestre2 ['Fisica'] = f2

        bimestre2 ['Promedio'] = promedio2/8
        notas.append(bimestre2)
        # ------------------------------------------------------
        # bim 3 --------------------------------------------------
        bimestre3 = {}
        bimestre3['bimestre'] = 3
        if(Matematicas.objects.filter(nombre_alumno = alumno,
        bimestre = 3).exists()):
            m3 = Matematicas.objects.filter(nombre_alumno = alumno,
            bimestre = 3).get()
            promedio3 = promedio3+m3.nota_mate # promedio bimestral
            bimestre3 ['Matematicas'] = m3.nota_mate
            mate = mate + m3.nota_mate
        else:
            m3 = 'NNI'
            bimestre3 ['Matematicas'] = m3

        if(Cultura.objects.filter(nombre_alumno = alumno,
        bimestre = 3).exists()):
            c3 = Cultura.objects.filter(nombre_alumno = alumno,
            bimestre = 3).get()
            promedio3 = promedio3+c3.nota_cultura # promedio bimestral
            bimestre3 ['Cultura'] = c3.nota_cultura
            cultura = cultura + c3.nota_cultura # variable para sumar los 240
        else:
            c3 = 'NNI'
            bimestre3 ['Cultura'] = c3

        if(Español.objects.filter(nombre_alumno = alumno,
        bimestre = 3).exists()):
            e3 = Español.objects.filter(nombre_alumno = alumno,
            bimestre = 3).get()
            promedio3 = promedio3+e3.nota_español # promedio bimestral
            bimestre3 ['Español'] = e3.nota_español
            español = español + e3.nota_español # variable para sumar 240
        else:
            e3 = 'NNI'
            bimestre3 ['Español'] = e3

        if(Ingles.objects.filter(nombre_alumno = alumno,
        bimestre = 3).exists()):
            i3 = Ingles.objects.filter(nombre_alumno = alumno,
            bimestre = 3).get()
            promedio3 = promedio3+i3.nota_ingles # promedio bimestral
            bimestre3 ['Ingles'] = i3.nota_ingles
            ingles = ingles + i3.nota_ingles # variable para sumar 240
        else:
            i3 = 'NNI'
            bimestre3 ['Ingles'] = i3

        if(Artistica.objects.filter(nombre_alumno = alumno,
        bimestre = 3).exists()):
            a3 = Artistica.objects.filter(nombre_alumno = alumno,
            bimestre = 3).get()
            promedio3 = promedio3+a3.nota_artistica # promedio bimestral
            bimestre3 ['Artistica'] = a3.nota_artistica
            artistica = artistica + a3.nota_artistica # variable para sumar 240
        else:
            a3 = 'NNI'
            bimestre3 ['Artistica'] = a3

        if(Productividad.objects.filter(nombre_alumno = alumno,
        bimestre = 3).exists()):
            p3 = Productividad.objects.filter(nombre_alumno = alumno,
            bimestre = 3).get()
            promedio3 = promedio3+p3.nota_productividad # promedio bimestral
            bimestre3 ['Productividad'] = p3.nota_productividad
            productividad = productividad + p3.nota_productividad # variable para sumar 240
        else:
            p3 = 'NNI'
            bimestre3 ['Productividad'] = p3

        if(Tecnologia.objects.filter(nombre_alumno = alumno,
        bimestre = 3).exists()):
            t3 = Tecnologia.objects.filter(nombre_alumno = alumno,
            bimestre = 3).get()
            promedio3 = promedio3+t3.nota_tecnologia # promedio bimestral
            bimestre3 ['Tecnologia'] = t3.nota_tecnologia
            tecnologia = tecnologia + t3.nota_tecnologia # variable para sumar 240
        else:
            t3 = 'NNI'
            bimestre3 ['Tecnologia'] = t3

        if(Fisica.objects.filter(nombre_alumno = alumno,
        bimestre = 3).exists()):
            f3 = Fisica.objects.filter(nombre_alumno = alumno,
            bimestre = 3).get()
            promedio3 = promedio3+f3.nota_fisica # promedio bimestral
            bimestre3 ['Fisica'] = f3.nota_fisica
            fisica = fisica + f3.nota_fisica # variable para sumar 240
        else:
            f3 = 'NNI'
            bimestre3 ['Fisica'] = f3

        bimestre3 ['Promedio'] = promedio3/8
        notas.append(bimestre3)
        # ------------------------------------------------------
        # bim 4 ------------------------------------------------
        bimestre4 = {}
        bimestre4['bimestre'] = 4
        if(Matematicas.objects.filter(nombre_alumno = alumno,
        bimestre = 4).exists()):
            m4 = Matematicas.objects.filter(nombre_alumno = alumno,
            bimestre = 4).get()
            promedio4 = promedio4+m4.nota_mate # promedio bimestral
            bimestre4 ['Matematicas'] = m4.nota_mate
            mate = mate + m4.nota_mate # variable para sumar 240
        else:
            m4 = 'NNI'
            bimestre4 ['Matematicas'] = m4

        if(Cultura.objects.filter(nombre_alumno = alumno,
        bimestre = 4).exists()):
            c4 = Cultura.objects.filter(nombre_alumno = alumno,
            bimestre = 4).get()
            promedio4 = promedio4+c4.nota_cultura # promedio bimestral
            bimestre4 ['Cultura'] = c4.nota_cultura
            cultura = cultura + c4.nota_cultura # variable para sumar los 240
        else:
            c4 = 'NNI'
            bimestre4 ['Cultura'] = c4

        if(Español.objects.filter(nombre_alumno = alumno,
        bimestre = 4).exists()):
            e4 = Español.objects.filter(nombre_alumno = alumno,
            bimestre = 4).get()
            promedio4 = promedio4+e4.nota_español # promedio bimestral
            bimestre4 ['Español'] = e4.nota_español
            español = español + e4.nota_español # variable para sumar 240
        else:
            e4 = 'NNI'
            bimestre4 ['Español'] = e4

        if(Ingles.objects.filter(nombre_alumno = alumno,
        bimestre = 4).exists()):
            i4 = Ingles.objects.filter(nombre_alumno = alumno,
            bimestre = 4).get()
            promedio4 = promedio4+i4.nota_ingles # promedio bimestral
            bimestre4 ['Ingles'] = i4.nota_ingles
            ingles = ingles + i3.nota_ingles # variable para sumar 240
        else:
            i4 = 'NNI'
            bimestre4 ['Ingles'] = i4

        if(Artistica.objects.filter(nombre_alumno = alumno,
        bimestre = 4).exists()):
            a4 = Artistica.objects.filter(nombre_alumno = alumno,
            bimestre = 4).get()
            promedio4 = promedio4+a4.nota_artistica # promedio bimestral
            bimestre4 ['Artistica'] = a4.nota_artistica
            artistica = artistica + a4.nota_artistica # variable para sumar 240
        else:
            a4 = 'NNI'
            bimestre4 ['Artistica'] = a4

        if(Productividad.objects.filter(nombre_alumno = alumno,
        bimestre = 4).exists()):
            p4 = Productividad.objects.filter(nombre_alumno = alumno,
            bimestre = 4).get()
            promedio4 = promedio4+p4.nota_productividad # promedio bimestral
            bimestre4 ['Productividad'] = p4.nota_productividad
            productividad = productividad + p4.nota_productividad # variable para sumar 240
        else:
            p4 = 'NNI'
            bimestre4 ['Productividad'] = p4

        if(Tecnologia.objects.filter(nombre_alumno = alumno,
        bimestre = 4).exists()):
            t4 = Tecnologia.objects.filter(nombre_alumno = alumno,
            bimestre = 4).get()
            promedio4 = promedio4+t4.nota_tecnologia # promedio bimestral
            bimestre4 ['Tecnologia'] = t4.nota_tecnologia
            tecnologia = tecnologia + t4.nota_tecnologia # variable para sumar 240
        else:
            t4 = 'NNI'
            bimestre4 ['Tecnologia'] = t4

        if(Fisica.objects.filter(nombre_alumno = alumno,
        bimestre = 4).exists()):
            f4 = Fisica.objects.filter(nombre_alumno = alumno,
            bimestre = 4).get()
            promedio4 = promedio4+f4.nota_fisica # promedio bimestral
            bimestre4 ['Fisica'] = f4.nota_fisica
            fisica = fisica + f4.nota_fisica # variable para sumar 240
        else:
            f4 = 'NNI'
            bimestre4 ['Fisica'] = f4

        bimestre4 ['Promedio'] = promedio4/8
        notas.append(bimestre4)

        total_promedio = promedio1/8 + promedio2/8 + promedio3/8 + promedio4/8


        total = [mate,español,ingles,cultura,productividad,artistica,tecnologia,fisica,total_promedio]

        return super(Informe_notas, self).get_context_data(
            pagezise = 'letter',
            title = 'notas_alumno', # Intentar concatenar nombre y apellido
            Alumno = inscripcion,
            notas = notas,
            total = total,
            **kwargs
        )
