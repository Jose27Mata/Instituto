from django.contrib import admin
from .models import *
from import_export import resources # para exportar e importar
from import_export.admin import ImportExportModelAdmin # para exportar e importar
# Register your models here.

class AsignacionResource(resources.ModelResource): # para exportar e importar
    class Meta:
        model = Asignacion
        model = Curso

class AdminAsignacion(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre_curso'] # para hacer busquedas en los informes
    list_display = ['nombre_curso', 'profesor', 'Imprimirinforme']

class AdminCurso(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['nombre', 'sueldo']

admin.site.register(Asignacion, AdminAsignacion)
admin.site.register(Curso, AdminCurso)
