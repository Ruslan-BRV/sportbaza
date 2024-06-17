from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Получаю настройки своего сайта
from django.conf.urls.static import static
from news import views
from news.views import regUser # Функция, которая будет обрабатывать все запросы на получения файлов

admin.site.site_header = 'Управление'
admin.site.site_title = "Административный сайт"
admin.site.index_title = "Добро пожаловать в панель управления"

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path("programms/", include("programms.urls")),
    path("news/", include("news.urls")),
    path("calculator/", include("calculator.urls")),
    path("registration/", regUser),
    path('users/', include('users.urls', namespace='users')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
      import debug_toolbar
      urlpatterns = [
          path('__debug__/', include(debug_toolbar.urls)),
          # другие URL-паттерны
      ] + urlpatterns