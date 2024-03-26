from django.urls import path
from calculator.views import calculator

urlpatterns = [
    path("", calculator, name='calculator')
]