from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Получаю настройки своего сайта
from django.conf.urls.static import static # Функция, которая будет обрабатывать все запросы на получения файлов

admin.site.site_header = 'Управление'
admin.site.site_title = "Административный сайт"
admin.site.index_title = "Добро пожаловать в панель управления"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("programms/", include("programms.urls")),
    path("", include("news.urls")),
    path("calculator/", include("calculator.urls")) 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
