from django.urls import path
from programms.views import mainPage

urlpatterns = [
    path("", mainPage)
]