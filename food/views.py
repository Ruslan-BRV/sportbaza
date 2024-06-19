from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class FoodView(TemplateView):
    template_name = 'food/food.html'