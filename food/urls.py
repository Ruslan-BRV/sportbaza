from django.urls import path
from food.views import FoodView

urlpatterns = [
    path("", FoodView.as_view()),
]