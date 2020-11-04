from django.contrib import admin
from .models import *
from import_export import resources # para exportar e importar
from import_export.admin import ImportExportModelAdmin # para exportar e importar

# Register your models here.
class InscripcionResource(resources.ModelResource): # para exportar e importar
    class Meta:
        model = Inscripcion
                        # se agrega para exportar e importar
class AdminInscripcion(ImportExportModelAdmin, admin.ModelAdmin): # para hacer una busqueda de un campo de otra app
    autocomplete_fields = ['nombre_alumno']
    resource_class = InscripcionResource
    list_display = ['nombre_alumno', 'id', 'grado', 'ciclo', 'detalle', 'Imprimirinforme', 'Imprimirnotas']
    list_filter = ['grado', 'ciclo']
    fieldsets = (
        ('Información Personal', {
            'fields': ((
                'fecha_ins', 'papeleria_completa', 'nombre_alumno',), (
                'grado', 'ciclo',), (
                ))
        }),
        ('Ubicación de Papelería', {
            'fields': ((
                'archivo', 'gabeta', 'folio',),
                )
        }),
        ('Detalle de la Inscripción', {
            'fields': ((
                'detalle',),
                )
        }),)

class AdminPago(admin.ModelAdmin): # para hacer una busqueda de un campo de otra app
    autocomplete_fields = ['nombre_alumno']
    list_display = ('nombre_alumno', 'fecha_pago',
    'tipo_pago', 'mostrarMonto', 'ImprimirinformeP')
    list_filter = ['tipo_pago']

admin.site.register(Inscripcion, AdminInscripcion) # aqui tambien se registra
admin.site.register(Pagos, AdminPago)
