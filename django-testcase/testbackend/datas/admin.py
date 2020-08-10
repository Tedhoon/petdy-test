from django.contrib import admin
from .models import Disease, NutrientData
from import_export.admin import ImportExportMixin

class DiseaseAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'desc')
    list_editable = ('desc', )
    fields = ('name', 'desc')
    search_fields = ('name', )
    pass

admin.site.register(Disease, DiseaseAdmin)


class NutrientDataAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'desc', )
    list_editable =  ('desc', )
    fields = ('name', 'desc', 'disease')
    search_fields = ('name', 'desc', 'disease')
    pass

admin.site.register(NutrientData, NutrientDataAdmin)