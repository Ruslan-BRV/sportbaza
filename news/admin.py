from django.contrib import admin
from news.models import News, Comment, Users

# Register your models here.
# admin.site.register(News)
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', News.bodyNew, 'upload_date')
    list_display_links = ('id', News.bodyNew, 'upload_date')
    search_fields = ('title',)
    # list_filter = ('typeProgramm',)
    ordering = ('id',)
    list_per_page = 10

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    pass