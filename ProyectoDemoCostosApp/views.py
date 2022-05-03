from django.shortcuts import render, HttpResponse
from ProyectoDemoCostosApp.models import OMC23Nivel1, OMC23Nivel2, OMC23Nivel3, OMC23Nivel4, OMC23Nivel5,OMC23Nivel6
# Create your views here.

def principal(request):

    OMC23Nivel1Todos = OMC23Nivel1.objects.all()
    OMC23Nivel2Todos = OMC23Nivel2.objects.all()
    OMC23Nivel3Todos = OMC23Nivel3.objects.all()
    OMC23Nivel4Todos = OMC23Nivel4.objects.all()
    OMC23Nivel5Todos = OMC23Nivel5.objects.all()
    OMC23Nivel6Todos = OMC23Nivel6.objects.all()
    
    return render(request, "ProyectoDemoCostosApp/principal.html", {"OMC23Nivel1Todos": OMC23Nivel1Todos, "OMC23Nivel2Todos": OMC23Nivel2Todos, 
                    "OMC23Nivel3Todos": OMC23Nivel3Todos, "OMC23Nivel4Todos": OMC23Nivel4Todos, "OMC23Nivel5Todos": OMC23Nivel5Todos, "OMC23Nivel6Todos": OMC23Nivel6Todos})