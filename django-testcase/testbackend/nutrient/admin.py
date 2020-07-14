from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Feed, Nutrient


class FeedAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'types', 'calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    list_editable = ( 'calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    fields = ('name', 'types', ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus'))
    search_fields = ('name', 'types')
    pass

admin.site.register(Feed, FeedAdmin)


class NutrientAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    list_editable = ( 'calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    fields = ('name', ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus'))
    search_fields = ('name', )
    pass

admin.site.register(Nutrient, NutrientAdmin)
