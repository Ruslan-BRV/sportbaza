from django.urls import path
from programms.views import main_page, detail_programm

urlpatterns = [
    path("", main_page, name='programms'),
    path('<int:card_id>/detail/', detail_programm, name='detail_programm')

]