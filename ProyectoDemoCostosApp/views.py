from django.shortcuts import render, HttpResponse
from ProyectoDemoCostosApp.models import Acronimo, AguaCemento, OMC23Nivel1, OMC23Nivel2, OMC23Nivel3, OMC23Nivel4, OMC23Nivel5,OMC23Nivel6, OmniClass23, OmniClass41, TipoConsistencia, TipoUniMed
from ProyectoDemoCostosApp.models import Materiales, Concreto, Esfuerzo, ValorEsfuerzo, TipoResistencia, AplPrincipales, TMA, Revenimiento, Densidad, SistColocacion, ClasExposicion, FlujoRev, CaracEspe, IonCloruro, FibraConcre, UnidadesMedida
# Create your views here.

def principal(request):
    
    return omniclass23(request)

def omniclass23(request): #FUNCION QUE SE TRAE TODOS LOS NIVELES

    '''
    OMC23Nivel1Todos = OMC23Nivel1.objects.all()
    OMC23Nivel2Todos = OMC23Nivel2.objects.all()
    OMC23Nivel3Todos = OMC23Nivel3.objects.all()
    OMC23Nivel4Todos = OMC23Nivel4.objects.all()
    OMC23Nivel5Todos = OMC23Nivel5.objects.all()
    OMC23Nivel6Todos = OMC23Nivel6.objects.all()'''

    listaOMC = OmniClass23.objects.all()

    return render(request, "ProyectoDemoCostosApp/principal.html", {"listaOMC": listaOMC})

    '''
    return render(request, "ProyectoDemoCostosApp/principal.html", {"OMC23Nivel1Todos": OMC23Nivel1Todos, "OMC23Nivel2Todos": OMC23Nivel2Todos, 
                    "OMC23Nivel3Todos": OMC23Nivel3Todos, "OMC23Nivel4Todos": OMC23Nivel4Todos, "OMC23Nivel5Todos": OMC23Nivel5Todos, "OMC23Nivel6Todos": OMC23Nivel6Todos})'''

def omniclass41(request):
    listaOMC = OmniClass41.objects.all()

    return render(request, "ProyectoDemoCostosApp/principal.html", {"listaOMC": listaOMC})
    

def obtenerNivelEspecifico(request, bandera, aux_nivel): #FUNCION PARA TRAER UN NIVEL EN ESPECIFICO

    if bandera == 1:
        OMCNivelEspecifico = OmniClass23.objects.filter(Nivel=aux_nivel)
    else:
        OMCNivelEspecifico = OmniClass41.objects.filter(Nivel=aux_nivel)

    return render(request, "ProyectoDemoCostosApp/principal.html", {"listaOMC": OMCNivelEspecifico})

def obtenerMaterial(request, id, numMat): #esta funcion por parametro va a re recibir el codigo de omniclass (Codigo)  y el numero identificador del material (numMat)
    if numMat == 614:
        return obtenerConcreto(request, id, numMat)
    else:
        pass

def obtenerConcreto(request, id, numMat): #esta funcion por parametro va a re recibir el codigo de omniclass (Codigo)  y el numero identificador del material (numMat)
    #datos = Materiales.objects.all() 
    datos = Concreto.objects.all() 
    #datos = Esfuerzo.objects.all()
    #datos = ValorEsfuerzo.objects.all()
    #datos = TipoResistencia.objects.all()
    #datos = AplPrincipales.objects.all()
    # datos = TMA.objects.all()
    #datos = Revenimiento.objects.all()
    #datos = Densidad.objects.all()
    #datos = SistColocacion.objects.all()
    #datos = ClasExposicion.objects.all()
    #datos = FlujoRev.objects.all()
    #datos = CaracEspe.objects.all()
    #datos = IonCloruro.objects.all()
    #datos = FibraConcre.objects.all()
    #datos = UnidadesMedida.objects.all()
    #datos = Acronimo.objects.all()
    #datos = TipoConsistencia.objects.all()
    #datos = TipoUniMed.objects.all()
    #datos = AguaCemento.objects.all()
    listaOMC = OmniClass23.objects.all()

    return render(request, "ProyectoDemoCostosApp/concreto.html", {"Datos": datos})

def obtenerConcreto(request, id, numMat):
    esfuer = request.get("esferzo")
