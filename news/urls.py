from django.urls import path
from news.views import newsPage, addLike, addDizlike, NewsPage

urlpatterns = [
    path("", NewsPage.as_view(), name="news"),
    path("dizlike/<int:news_id>", addDizlike),
    path("like/<int:news_id>", addLike) 
]
