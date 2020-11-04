from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class AdminResource(resources.ModelResource): # para exportar e importar
    class Meta:
        model = Alumno
        model = Encargado

# class EncargadoResource(resources.ModelResource): # para exportar e importar
#    class Meta:
#        model = Encargado

class AdminAlumno(ImportExportModelAdmin, admin.ModelAdmin): # para hacer una busqueda de un campo de otra app
    search_fields = ['nombre'] # para hacer busquedas en los informes
    autocomplete_fields = ['nombre_encargado']
    list_display = ('nombre', 'estado', 'codigo_personal', 'getAtributo',# para mostrar esos campos en los informes
    'direccion', 'telefono', 'Imprimirinforme')
    list_filter = ['sexo', 'estado']
    fieldsets = (
        ('Información Personal', {
            'fields': ((
                'estado', 'nombre', 'dpi'), (
                'codigo_personal', 'sexo', 'fecha_nac',), (
                 'nombre_encargado',))
        }),
        ('Información de Contacto', {
            'fields': ((
                'direccion', 'telefono'),
                )
        }),)
    resource_class = AdminResource
    list_filter = ['sexo', 'direccion']

class AdminEncargado(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre_encargado'] # para hacer busquedas en los informes
    list_display = ('nombre_encargado', 'direccion',# para mostrar esos campos en los informes
    'dpi', 'telefono', 'Imprimirinforme')
    resource_class = AdminResource
    fieldsets = (
        ('Información Personal', {
            'fields': ((
                'nombre_encargado', 'fecha_nac',), (
                'dpi',), (
                ))
        }),
        ('Información de Contacto', {
            'fields': ((
                'direccion', 'telefono'),
                )
        }),)
    list_filter = ['direccion']
admin.site.register(Alumno, AdminAlumno)
admin.site.register(Encargado, AdminEncargado)
