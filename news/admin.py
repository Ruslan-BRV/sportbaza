from django.contrib import admin
from news.models import News

# Register your models here.
# admin.site.register(News)
@admin.register(News)
class ProgrammsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', News.bodyNew, 'upload_date')
    list_display_links = ('id', News.bodyNew, 'upload_date')
    search_fields = ('title',)
    # list_filter = ('typeProgramm',)
    ordering = ('id',)
    list_per_page = 10
