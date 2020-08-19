from django.contrib import admin
from .models import Disease, NutrientData, DogBreed, AgeRange
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
    # list_editable =  ('desc', )
    # fields = ('name', 'desc', )
    search_fields = ('name', 'desc', )
    pass

admin.site.register(NutrientData, NutrientDataAdmin)

class DogBreedAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_editable =  ('name',)
    # fields = ('name', )
    search_fields = ('name', )
    pass

admin.site.register(DogBreed, DogBreedAdmin)

class AgeRangeAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'desc')
    list_editable =  ('desc',)
    fields = ('name', 'slug', 'desc', 'min_age', 'max_age', ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'l', 'n', 'o', 'p'))
    search_fields = ('name', )
    pass

admin.site.register(AgeRange, AgeRangeAdmin)

# ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'l')