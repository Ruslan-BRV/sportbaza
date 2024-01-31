from django.shortcuts import render
from programms.models import Programms
# Create your views here.

def mainPage(request):
    listProgramms = Programms.objects.all()

    context = {
        "listProgramms": listProgramms
    }

    return render(request, "programms/index.html", context=context)