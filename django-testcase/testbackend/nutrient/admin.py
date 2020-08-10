from django.contrib import admin
from import_export.admin import ImportExportMixin
from .models import Feed, Snack, Nutrient, ExchangedFeed, ExchangedNutrient, ExchangedSnack


class FeedAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'types', 'calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    list_editable = ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    fields = ('name', 'types', ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus'))
    search_fields = ('name', 'types')
    pass

admin.site.register(Feed, FeedAdmin)


class NutrientAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    list_editable = ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    fields = ('name', ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus'))
    search_fields = ('name', )
    pass

admin.site.register(Nutrient, NutrientAdmin)



class ExchangedFeedAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'types', 'calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    list_editable = ( 'calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    fields = ('name', 'types', ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus'))
    search_fields = ('name', 'types')
    pass

admin.site.register(ExchangedFeed, ExchangedFeedAdmin)

class ExchangedNutrientAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    list_editable = ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    fields = ('name', ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus'))
    search_fields = ('name', )
    pass

admin.site.register(ExchangedNutrient, ExchangedNutrientAdmin)


class SnackAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    list_editable = ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    fields = ('name', ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus'))
    search_fields = ('name', )
    pass

admin.site.register(Snack, SnackAdmin)

class ExchangedSnackAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    list_editable = ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus')
    fields = ('name', ('calorie', 'moisture', 'crude_protein', 'crude_fat', 'crude_fiber', 'crude_ash', 'calcium', 'phosphorus'))
    search_fields = ('name', )
    pass

admin.site.register(ExchangedSnack, ExchangedSnackAdmin)