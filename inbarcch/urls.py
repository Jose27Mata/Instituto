"""inbarcch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Archivo.views import Informe_inscripcion
from Archivo.views import Informe_pagos
from Informacion.views import Informe_alumnos
from Informacion.views import Informe_encargado
from Personal.views import Informe_profesor
from Personal.views import Informe_otro
from Curso.views import Informe_curso
from Archivo.views import Informe_notas
from django.conf.urls import url
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    # path de los informes
    url(r"^Informe_inscripcion/(?P<id>)", Informe_inscripcion.as_view()),
    url(r"^Informe_pagos/(?P<id>)", Informe_pagos.as_view()),
    url(r"^Informe_alumnos/(?P<id>)", Informe_alumnos.as_view()),
    url(r"^Informe_profesor/(?P<id>)", Informe_profesor.as_view()),
    url(r"^Informe_otro/(?P<id>)", Informe_otro.as_view()),
    url(r"^Informe_encargado/(?P<id>)", Informe_encargado.as_view()),
    url(r"^Informe_curso/(?P<id>)", Informe_curso.as_view()),
    url(r"^Informe_notas/(?P<id>)", Informe_notas.as_view()),
]

# Custom titles para el admin
admin.site.site_header = 'Administrador de INBARCCH'
admin.site.index_title = 'Administración del Instituto Básico por Cooperativa Chanmagua'
admin.site.site_title = 'INBARCCH'
