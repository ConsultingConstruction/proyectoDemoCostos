from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from ProyectoDemoCostosApp.models import Acronimo, AguaCemento, OMC23Nivel1, OMC23Nivel2, OMC23Nivel3, OMC23Nivel4, OMC23Nivel5,OMC23Nivel6, OmniClass23, OmniClass41, TipoConsistencia, TipoUniMed
from ProyectoDemoCostosApp.models import Materiales, Concreto, Esfuerzo, ValorEsfuerzo, TipoResistencia, AplPrincipales, TMA, Revenimiento, Densidad, SistColocacion, ClasExposicion, FlujoRev, CaracEspe, IonCloruro, FibraConcre, UnidadesMedida
from ProyectoDemoCostosApp.forms import CaracEspeForm
from django.contrib import messages
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

def obtenerMaterial(request, idOmc, numMat): #esta funcion por parametro va a re recibir el codigo de omniclass (Codigo)  y el numero identificador del material (numMat)
    if numMat == 614:
        return obtenerConcreto(request, idOmc, numMat)
    else:
        pass

def obtenerConcreto(request, idOmc, pNumMat): #esta funcion por parametro va a re recibir el identificador del registro que se selecciono  y el numero identificador del material (numMat)
    
    registroOMC = get_object_or_404(OmniClass23, pk=idOmc)
    if request.method == 'POST':
        formCaracEspe = CaracEspeForm(request.POST)
        if formCaracEspe.is_valid():
            #--HACER FUNCION O TRIGGER O PROCEDURE QUE VALIDE QUE EL CONCRETO NO EXISTE YA
            #--INSERTAR EN LA TABLA DE MATERIALES
                #--hacer lo correspondiente para generar el consecutivo
                #--hacer lo correspondiente para la descripcion corta
            #descriCorta = 
                #--hacer lo correspondiente para la descripcion larga
            #cadena1 ='numMat:' + str(pNumMat) + ',codigoOmc:' + registroOMC.Codigo + ',Consecutivo:' + ',descriCorta:' + ',descriLarga:' + ',Comentarios:' + str(request.POST.get('comentarios')) + ',PalabrasCve:' + str(request.POST.get('palabrasCve')) + ',codigoBimsa:' + ',fk_Omc23:' + str(idOmc) + ',fk_omc41:'
            #print(cadena1)
            materiales = Materiales(numMat = pNumMat, codigoOmc = registroOMC.Codigo, Consecutivo = None, descriCorta = None, descriLarga = None, Comentarios = request.POST.get('comentarios'), palabrasCve = request.POST.get('palabrasCve'), codigoBimsa = None, fk_Omc23 = registroOMC, fk_Omc41 = None)
            materiales.save()
            #--INSERTAR EN LA TABLA DE CONCRETO
            #cadena2 = 'numMat:' + str(pNumMat) + ',Codigo:' + str(request.POST.get('codigoOmc')) + ',fk_Material:' + ',fk_ClasExpo:' + str(request.POST.get('idClasExpo')) + ',fk_SistColoc:' + str(request.POST.get('idSistColoc')) + ',fk_Densidad:' + str(request.POST.get('idDensidad')) + ',fk_Reven:' + str(request.POST.get('idReven')) + ',fk_FlujoRev:' + str(request.POST.get('idFlujoRev')) + ',fk_FibraConcre:' + str(request.POST.get('idFibraConcre')) + ',fk_ValEsf:' + str(request.POST.get('idValEsf')) + ',fk_Tma:' + str(request.POST.get('idTma')) + ',fk_AplPrinc:' + str(request.POST.get('idAplPrinc'))
            #print(cadena2)
            registroClasExpo = None
            registroDensidad = None
            registroFlujoRev = None
            registroFibraCon = None
            registroAplPrin = None
            if request.POST.get('idClasExpo'):
                registroClasExpo = get_object_or_404(ClasExposicion,pk = request.POST.get('idClasExpo'))
            registroSistColoc = get_object_or_404(SistColocacion,pk = request.POST.get('idSistColoc'))
            if request.POST.get('idDensidad'):
                registroDensidad = get_object_or_404(Densidad,pk = request.POST.get('idDensidad'))
            registroReven = get_object_or_404(Revenimiento, pk = request.POST.get('idReven'))
            if request.POST.get('idFlujoRev'):
                registroFlujoRev = get_object_or_404(FlujoRev, pk = request.POST.get('idFlujoRev'))
            if request.POST.get('idFibraConcre'):
                registroFibraCon = get_object_or_404(FibraConcre, pk = request.POST.get('idFibraConcre'))
            registroValEsf = get_object_or_404(ValorEsfuerzo, pk = request.POST.get('idValEsf'))
            registroTma = get_object_or_404(TMA, pk = request.POST.get('idTma'))
            if request.POST.get('idAplPrinc'):
                registroAplPrin = get_object_or_404(AplPrincipales, pk = request.POST.get('idAplPrinc'))

            concreto = Concreto(numMat = pNumMat, Codigo = registroOMC.Codigo, fk_Material = materiales, fk_ClasExpo = registroClasExpo, fk_SistColoc = registroSistColoc, fk_Densidad = registroDensidad, fk_Reven = registroReven, fk_FlujoRev = registroFlujoRev, fk_FibraConcre = registroFibraCon, fk_ValEsf = registroValEsf, fk_Tma = registroTma, fk_AplPrinc = registroAplPrin)
            concreto.save()
            #--INSERTAR EN LA TABLA DE CARACESPE
            #newForm = formCaracEspe.save(commit=False)
            #cadena3 = str(newForm.Acronimo) + '-' + str(newForm.modElast) + '-' + str(newForm.Edad) + '-' + str(newForm.absorcionCap) + '-' + str(newForm.Acronimo2) + '-' + str(newForm.trabaExtend) + '-' + str(newForm.Clase) + '-' + str(newForm.Color) + '-' + str(newForm.Comportamiento) + '-' + str(newForm.conAire) + '-' + str(newForm.conIonClor) + '-' + str(request.POST.get('idIonClor') + '-' + str(newForm.tiempoPrueba))
            #print(cadena3)
            newForm = formCaracEspe.save(commit=False)
            if request.POST.get('idIonClor'):
                registroIonClor = get_object_or_404(IonCloruro, pk = request.POST.get('idIonClor'))
                newForm.fk_IonClor = registroIonClor
            newForm.fk_Concreto = concreto
            newForm.save()
            return redirect('Principal')
        else:
            messages.success(request, 'Ocurrio un error!')
        

    else:
        #datMateriales = Materiales.objects.all() 
        #datConcreto = Concreto.objects.all() 
        datEsfuerzo = Esfuerzo.objects.all()
        datValorEsfuerzo = ValorEsfuerzo.objects.all()
        datTipoResistencia = TipoResistencia.objects.all()
        datAplPrincipales = AplPrincipales.objects.all()
        daTma = TMA.objects.all()
        datRevenimiento = Revenimiento.objects.all()
        datDensidad = Densidad.objects.all()
        datSisColocacion = SistColocacion.objects.all()
        datClasExposicion = ClasExposicion.objects.all()
        datFlujoRev = FlujoRev.objects.all()
        #datCaracEspe = CaracEspe.objects.all()
        datIonCloruro = IonCloruro.objects.all()
        datFibraConcre = FibraConcre.objects.all()
        datUnidadesMedida = UnidadesMedida.objects.all()
        #datAcronimo = Acronimo.objects.all()
        #daTipoConsistencia = TipoConsistencia.objects.all()
        #daTipoUniMed = TipoUniMed.objects.all()
        #datAguaCemento = AguaCemento.objects.all()
        listaOMC = OmniClass23.objects.all()
        formCaracEspe = CaracEspeForm()
        #cadena = 'aqui concatenacion ' + str(123)
        #print(cadena)

    return render(request, "ProyectoDemoCostosApp/concreto.html", {'listaOMC': listaOMC, 'registroOMC': registroOMC, 'formCaracEspe':formCaracEspe,'datEsfuerzo': datEsfuerzo,'datValorEsfuerzo': datValorEsfuerzo, 'datTipoResistencia':datTipoResistencia, 'datAplPrincipales':datAplPrincipales, 'daTma':daTma, 'datRevenimiento':datRevenimiento, 'datDensidad':datDensidad, 'datSisColocacion':datSisColocacion,'datClasExposicion':datClasExposicion,'datFlujoRev':datFlujoRev,'datIonCloruro':datIonCloruro,'datFibraConcre':datFibraConcre,'datUnidadesMedida':datUnidadesMedida})

