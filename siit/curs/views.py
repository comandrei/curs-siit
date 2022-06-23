from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import Student, Curs

# Create your views here.
def hello_world(request):
    return HttpResponse("Hello World!")


def show_students(request):
    try:
        an_cerut = int(request.GET['an'])
        lista_studenti = Student.objects.filter(an__lte=an_cerut,)
    except KeyError:
        lista_studenti = Student.objects.all()

    try:
        nume = request.GET['nume']
        lista_studenti = lista_studenti.filter(nume__startswith=nume)
    except KeyError:
        pass
    
    promoveaza = request.GET.get("promoveaza")
    if promoveaza is not None:
        lista_studenti.update(an=2)
        # Student.objects.update(an=2) - va modifica toate intrarile din DB
    sterge = request.GET.get("sterge")
    if sterge is not None:
        print(sterge)
        lista_studenti.delete()
        #  Student.objects.delete() - va sterge toate intrarile
    lista_studenti = lista_studenti.order_by("-nume")

    #lista_studenti = Student.objects.boboci()

    context = {
        'studenti': lista_studenti,
        'mesaj': 'Salut'
    }

    return render(request, "list_students.html", context)


def show_curs(request):
    # import pdb; pdb.set_trace()
    # import ipdb; ipdb.set_trace() # pip install ipdb
    id_curs = int(request.GET.get('curs', 0))
    curs = Curs.objects.get(id=id_curs)
    studenti = curs.student_set.all()
    context = {
        'studenti': studenti
    }
    return render(request, "list_curs.html", context)