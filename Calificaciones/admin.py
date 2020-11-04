from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class AdminResource(resources.ModelResource): # para exportar e importar
    class Meta:
        model = Matematicas
        model = Cultura
        model = Español
        model = Ingles
        model = Artistica
        model = Productividad
        model = Tecnologia
        model = Fisica


class AdminMatematicas(ImportExportModelAdmin, admin.ModelAdmin): # para hacer una busqueda de un campo de otra app
    autocomplete_fields = ['nombre_alumno']
    search_fields = ['nombre_alumno'] # para hacer busquedas en los informes
    list_display = ('nombre_alumno', 'fecha', 'ciclo', 'bimestre', 'getNota_Mate')
    date_hierarchy = 'fecha'
    list_filter = ['ciclo', 'bimestre', 'fecha']
    fieldsets = (
        ('Información Personal', {
            'fields': ((
                'fecha', 'nombre_alumno',), (
                'ciclo', 'bimestre',), (
                ))
        }),
        ('Punteo y detales', {
            'fields': ((
                'nota_mate', 'detalle',),
                )
        }),)
    resource_class = AdminResource

class AdminCultura(ImportExportModelAdmin, admin.ModelAdmin): # para hacer una busqueda de un campo de otra app
    autocomplete_fields = ['nombre_alumno']
    search_fields = ['nombre_alumno'] # para hacer busquedas en los informes
    list_display = ('nombre_alumno', 'fecha', 'ciclo', 'bimestre', 'getNota_Cultura')
    list_filter = ['ciclo', 'bimestre', 'fecha']
    date_hierarchy = 'fecha'
    fieldsets = (
        ('Información Personal', {
            'fields': ((
                'fecha', 'nombre_alumno',), (
                'ciclo', 'bimestre',), (
                ))
        }),
        ('Punteo y detales', {
            'fields': ((
                'nota_cultura', 'detalle',),
                )
        }),)
    resource_class = AdminResource

class AdminEspañol(ImportExportModelAdmin, admin.ModelAdmin): # para hacer una busqueda de un campo de otra app
    autocomplete_fields = ['nombre_alumno']
    search_fields = ['nombre_alumno'] # para hacer busquedas en los informes
    list_display = ('nombre_alumno', 'fecha', 'ciclo', 'bimestre', 'getNota_Español')
    list_filter = ['ciclo', 'bimestre', 'fecha']
    date_hierarchy = 'fecha'
    fieldsets = (
    ('Información Personal', {
        'fields': ((
            'fecha', 'nombre_alumno',), (
            'ciclo', 'bimestre',), (
            ))
    }),
    ('Punteo y detales', {
        'fields': ((
            'nota_español', 'detalle',),
            )
    }),)
    resource_class = AdminResource

class AdminIngles(ImportExportModelAdmin, admin.ModelAdmin): # para hacer una busqueda de un campo de otra app
    autocomplete_fields = ['nombre_alumno']
    search_fields = ['nombre_alumno'] # para hacer busquedas en los informes
    list_display = ('nombre_alumno', 'fecha', 'ciclo', 'bimestre', 'getNota_Ingles')
    list_filter = ['ciclo', 'bimestre', 'fecha']
    date_hierarchy = 'fecha'
    fieldsets = (
        ('Información Personal', {
            'fields': ((
                'fecha', 'nombre_alumno',), (
                'ciclo', 'bimestre',), (
                ))
        }),
        ('Punteo y detales', {
            'fields': ((
                'nota_ingles', 'detalle',),
                )
        }),)
    resource_class = AdminResource

class AdminArtistica(ImportExportModelAdmin, admin.ModelAdmin): # para hacer una busqueda de un campo de otra app
    autocomplete_fields = ['nombre_alumno']
    search_fields = ['nombre_alumno'] # para hacer busquedas en los informes
    list_display = ('nombre_alumno', 'fecha', 'ciclo', 'bimestre', 'getNota_Artistica')
    list_filter = ['ciclo', 'bimestre', 'fecha']
    date_hierarchy = 'fecha'
    fieldsets = (
        ('Información Personal', {
            'fields': ((
                'fecha', 'nombre_alumno',), (
                'ciclo', 'bimestre',), (
                ))
        }),
        ('Punteo y detales', {
            'fields': ((
                'nota_artistica', 'detalle',),
                )
        }),)
    resource_class = AdminResource

class AdminProductividad(ImportExportModelAdmin, admin.ModelAdmin): # para hacer una busqueda de un campo de otra app
    autocomplete_fields = ['nombre_alumno']
    search_fields = ['nombre_alumno'] # para hacer busquedas en los informes
    list_display = ('nombre_alumno', 'fecha', 'ciclo', 'bimestre', 'getNota_Productividad')
    list_filter = ['ciclo', 'bimestre', 'fecha']
    date_hierarchy = 'fecha'
    fieldsets = (
        ('Información Personal', {
            'fields': ((
                'fecha', 'nombre_alumno',), (
                'ciclo', 'bimestre',), (
                ))
        }),
        ('Punteo y detales', {
            'fields': ((
                'nota_productividad', 'detalle',),
                )
        }),)
    resource_class = AdminResource

class AdminTecnologia(ImportExportModelAdmin, admin.ModelAdmin): # para hacer una busqueda de un campo de otra app
    autocomplete_fields = ['nombre_alumno']
    search_fields = ['nombre_alumno'] # para hacer busquedas en los informes
    list_display = ('nombre_alumno', 'fecha', 'ciclo', 'bimestre', 'getNota_Tecnologia')
    list_filter = ['ciclo', 'bimestre', 'fecha']
    date_hierarchy = 'fecha'
    fieldsets = (
        ('Información Personal', {
            'fields': ((
                'fecha', 'nombre_alumno',), (
                'ciclo', 'bimestre',), (
                ))
        }),
        ('Punteo y detales', {
            'fields': ((
                'nota_tecnologia', 'detalle',),
                )
        }),)
    resource_class = AdminResource

class AdminFisica(ImportExportModelAdmin, admin.ModelAdmin): # para hacer una busqueda de un campo de otra app
    autocomplete_fields = ['nombre_alumno']
    search_fields = ['nombre_alumno'] # para hacer busquedas en los informes
    list_display = ('nombre_alumno', 'fecha', 'ciclo', 'bimestre', 'getNota_Fisica')
    list_filter = ['ciclo', 'bimestre', 'fecha']
    date_hierarchy = 'fecha'
    fieldsets = (
        ('Información Personal', {
            'fields': ((
                'fecha', 'nombre_alumno',), (
                'ciclo', 'bimestre',), (
                ))
        }),
        ('Punteo y detales', {
            'fields': ((
                'nota_fisica', 'detalle',),
                )
        }),)
    resource_class = AdminResource

admin.site.register(Matematicas, AdminMatematicas)
admin.site.register(Cultura, AdminCultura)
admin.site.register(Español, AdminEspañol)
admin.site.register(Ingles, AdminIngles)
admin.site.register(Artistica, AdminArtistica)
admin.site.register(Productividad, AdminProductividad)
admin.site.register(Tecnologia, AdminTecnologia)
admin.site.register(Fisica, AdminFisica)
