from django.urls import path
from news.views import newsPage

urlpatterns = [
    path("", newsPage)
]
