from django.shortcuts import get_object_or_404, render
from programms.models import Programms, TypeProgramms
# Create your views here.

def main_page(request):
    type_list = TypeProgramms.objects.all()
    type = request.GET.get('type', 'full')
    if type == 'full':
        list_programms = Programms.objects.all()
    else:
        list_programms = Programms.objects.filter(typeProgramm=f'{type}')

    context = {
        "list_programms": list_programms,
        "type_list": type_list
    }

    return render(request, "programms/index.html", context=context)

def detail_programm(request, card_id):
    programm = get_object_or_404(Programms, pk=card_id)

    context = {
        "programm": programm,
    }

    return render(request, "programms/detail_programm.html", context=context)
