from django.shortcuts import get_object_or_404, render
from programms.models import Programms
# Create your views here.

def main_page(request):
    list_programms = Programms.objects.all()

    context = {
        "list_programms": list_programms
    }

    return render(request, "programms/index.html", context=context)

def detail_programm(request, card_id):
    programm = get_object_or_404(Programms, pk=card_id)

    context = {
        "programm": programm,
    }

    return render(request, "programms/detail_programm.html", context=context)
