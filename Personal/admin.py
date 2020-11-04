from django.contrib import admin
from .models import *
from Curso.models import Asignacion
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# Poner otro campo de otra App y modelo
class AsignacionesInline(admin.TabularInline):
    # Modelo el cual se mostrara en linea
    model = Asignacion
    # Instancias extras a crear
    extra = 0
    # Instancias Minimas a crear
    min_num = 0

class AdminResource(resources.ModelResource): # para exportar e importar
    class Meta:
        model = Profesor
        model = Otros

class AdminProfesor(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre'] # para hacer busquedas en los informes
    list_display = ('nombre', 'estado', 'codigo',  # para mostrar esos campos en los informes
    'direccion', 'telefono', 'Sueldo', 'Imprimirinforme')
    fieldsets = (
    ('Información Personal', {
        'fields': ((
            'estado', 'nombre',), (
            'codigo', 'fecha_nac', 'dpi',), (
            ))
    }),
    ('Información de Contacto', {
        'fields': ((
            'direccion', 'telefono',),
            )
    }),)
    inlines = [AsignacionesInline,]
    resource_class = AdminResource

class AdminOtros(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre'] # para hacer busquedas en los informes
    list_display = ('nombre', 'estado', 'puesto', 'mostrarMonto',  # para mostrar esos campos en los informes
    'direccion', 'telefono', 'Imprimirinforme')
    fieldsets = (
    ('Información Personal', {
        'fields': ((
            'estado', 'nombre',), (
            'puesto', 'fecha_nac', 'dpi',), (
            ))
    }),
    ('Información de Contacto', {
        'fields': ((
            'direccion', 'telefono', 'sueldo',),
            )
    }),)
    resource_class = AdminResource

admin.site.register(Profesor, AdminProfesor)
admin.site.register(Otros, AdminOtros)
