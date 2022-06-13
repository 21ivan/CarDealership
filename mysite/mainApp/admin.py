from django.contrib import admin

# Register your models here.
from mainApp.models import Brand, Car, Info


class BrandAdmin(admin.ModelAdmin):
    list_display = ('model', 'price', 'year',)
    list_filter = ('year', 'engine_type',)
    list_editable = ('price', )
    # list_display_links = ('update',)


# admin.site.register(BrandAdmin)
admin.site.register(Brand)
admin.site.register(Car)
admin.site.register(Info)
