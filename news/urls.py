from django.urls import path
from news.views import newsPage, addLike, addDizlike

urlpatterns = [
    path("", newsPage),
    path("dizlike/<int:news_id>", addDizlike),
    path("like/<int:news_id>", addLike),
]
