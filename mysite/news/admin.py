from django.contrib import admin
from .models import Articles


# class ArticlesAdmin(admin.ModelAdmin):
#     list_display = ('title', 'update', 'timestamp')
#     list_filter = ('update', 'timestamp')
#     list_editable = ('title',)
#     list_display_links = ('update',)


admin.site.register(Articles)

