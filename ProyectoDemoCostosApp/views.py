from asyncio.windows_events import NULL
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib import messages
from django.db import connection
from ProyectoDemoCostosApp.models import Acronimo, AguaCemento, OMC23Nivel1, OMC23Nivel2, OMC23Nivel3, OMC23Nivel4, OMC23Nivel5,OMC23Nivel6, OmniClass23, OmniClass41, TipoConsistencia, TipoUniMed
from ProyectoDemoCostosApp.models import Materiales, Concreto, Esfuerzo, ValorEsfuerzo, TipoResistencia, AplPrincipales, TMA, Revenimiento, Densidad, SistColocacion, ClasExposicion, FlujoRev, CaracEspe, IonCloruro, FibraConcre, UnidadesMedida
from ProyectoDemoCostosApp.forms import CaracEspeForm

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
    #--hacer lo correspondiente para generar el consecutivo
    ultimoRegistro = Materiales.objects.all().last()
    ultimoRegistro = generarConsecutivo(ultimoRegistro.Consecutivo)
    #print('consecutivo:' + ultimoRegistro)
    if request.method == 'POST':
        formCaracEspe = CaracEspeForm(request.POST)
        if formCaracEspe.is_valid():
            #--VALIDAR SI EXISTE EL CONCRETO
            #>>HACER FUNCION O TRIGGER O PROCEDURE QUE VALIDE QUE EL CONCRETO NO EXISTE YA
            #--SE GENERA LA DESCRIPCION CORTA Y LARGA
            registroEsfuerzo = ''
            registroUMD = '' 
            registroUMFR = ''
            registroAplPrin = None
            cadRegistroAplPrin = ''
            registroDensidad = None
            cadRegistroDensidad = ''
            registroClasExpo = None
            cadRegistroClasExpo = ''
            registroFlujoRev = None
            cadRegistroFlujoRev = ''
            registroFibraCon = None
            cadRegistroFibraCon = ''
            registroIonClor = None
            cadRegistroIonClor = '' 
            if request.POST.get('idEsfuerzo'):
                registroEsfuerzo = get_object_or_404(Esfuerzo,pk = request.POST.get('idEsfuerzo'))
                registroEsfuerzo = registroEsfuerzo.tipoEsfuerzo
            registroValEsf = get_object_or_404(ValorEsfuerzo, pk = request.POST.get('idValEsf'))
            registroUMVE = get_object_or_404(UnidadesMedida, pk = request.POST.get('idUniMedVE'))
            registroTipoResist = get_object_or_404(TipoResistencia, pk = request.POST.get('idTipoResist'))
            if request.POST.get('idAplPrinc'):
                registroAplPrin = get_object_or_404(AplPrincipales, pk = request.POST.get('idAplPrinc'))
                cadRegistroAplPrin = registroAplPrin.aplicaciones
            registroTma = get_object_or_404(TMA, pk = request.POST.get('idTma'))
            registroUMTMA = get_object_or_404(UnidadesMedida, pk = request.POST.get('idUniMedTMA'))
            registroReven = get_object_or_404(Revenimiento, pk = request.POST.get('idReven'))
            registroUMR = get_object_or_404(UnidadesMedida, pk = request.POST.get('idUniMedR'))
            if request.POST.get('idDensidad'):
                registroDensidad = get_object_or_404(Densidad,pk = request.POST.get('idDensidad'))
                cadRegistroDensidad = 'Densidad=' + str(registroDensidad.valDensidad).strip()
            if request.POST.get('idUniMedD'):
                registroUMD = get_object_or_404(UnidadesMedida, pk = request.POST.get('idUniMedD'))
                registroUMD = registroUMD.Unidad
            registroSistColoc = get_object_or_404(SistColocacion,pk = request.POST.get('idSistColoc'))
            if request.POST.get('idClasExpo'):
                registroClasExpo = get_object_or_404(ClasExposicion,pk = request.POST.get('idClasExpo'))
                cadRegistroClasExpo = 'ClaseExp=' + str(registroClasExpo.Clase).strip()
            if request.POST.get('idFlujoRev'):
                registroFlujoRev = get_object_or_404(FlujoRev, pk = request.POST.get('idFlujoRev'))
                cadRegistroFlujoRev = 'FlujoRev=' + str(registroFlujoRev.valFluRev).strip()
            if request.POST.get('idUniMedFR'):
                registroUMFR = get_object_or_404(UnidadesMedida, pk = request.POST.get('idUniMedFR'))
                registroUMFR = registroUMFR.Unidad
            if request.POST.get('idFibraConcre'):
                registroFibraCon = get_object_or_404(FibraConcre, pk = request.POST.get('idFibraConcre'))
                cadRegistroFibraCon = registroFibraCon.Fibras
            if request.POST.get('idIonClor'):
                registroIonClor = get_object_or_404(IonCloruro, pk = request.POST.get('idIonClor'))
                cadRegistroIonClor = registroIonClor.cargaPesada
            newForm = formCaracEspe.save(commit=False)
            conector = ' '
            
            auxDescriCorta = str(registroOMC.descriSpa).strip() + conector + str(registroEsfuerzo).strip() + conector + 'fc=' + str(registroValEsf.Valor).strip() + str(registroUMVE.Unidad).strip() + conector + str(registroTipoResist.Tipo).strip() + conector + str(cadRegistroAplPrin).strip() + conector + 'Tma=' + str(registroTma.valTma).strip() + str(registroUMTMA.Unidad).strip() + conector + 'Rev=' + str(registroReven.valRev).strip() + str(registroUMR.Unidad).strip() + conector + cadRegistroDensidad + str(registroUMD).strip() + conector + str(registroSistColoc.tipoSistema).strip() + conector + cadRegistroClasExpo + conector + cadRegistroFlujoRev + str(registroUMFR).strip()
            cadDescriCorta = auxDescriCorta[0:100]
            cadDescriLarga = auxDescriCorta + conector + ValidaCadena('Abrev=',newForm.Acronimo,'') + conector + ValidaCadena('Modulo de Elasticidad=',newForm.modElast,'') + conector + ValidaCadena('Edad=',newForm.Edad,'dias') + conector + ValidaCadena('Absorción Capilar=',newForm.absorcionCap,'') + conector + ValidaCadena('Abrev2=',newForm.Acronimo2,'') + conector + ValidaCadena('Trabajabilidad Extendidaa=',newForm.trabaExtend,'hrs') + conector + ValidaCadena('Clase=',newForm.Clase,'') + conector + ValidaCadena('Color=',newForm.Color,'') + conector + ValidaCadena('Comportamiento=',newForm.Comportamiento,'') + conector + ValidaCadena('Contenido de aire=',newForm.conAire,'%') + conector + ValidaCadena('Contenido de Ion Cloruro=',newForm.conIonClor,'%') + conector + ValidaCadena('Ion Cloruro=',cadRegistroIonClor, 'coulomb') + conector + ValidaCadena('Tiempo de prueba del ensayo Ion Cloruro=',newForm.tiempoPrueba,'dias') + conector + ValidaCadena('Fibra=',cadRegistroFibraCon,'') + conector + ValidaCadena('Comentarios=',request.POST.get('comentarios'),'') + conector + ValidaCadena('Palabras Clave=',request.POST.get('palabrasCve'),'')
            #--INSERTAR EN LA TABLA DE MATERIALES
            #cadena1 ='numMat:' + str(pNumMat) + ',codigoOmc:' + registroOMC.Codigo + ',Consecutivo:' + ',descriCorta:' + ',descriLarga:' + ',Comentarios:' + str(request.POST.get('comentarios')) + ',PalabrasCve:' + str(request.POST.get('palabrasCve')) + ',codigoBimsa:' + ',fk_Omc23:' + str(idOmc) + ',fk_omc41:'
            #print(descriLarga)
            materiales = Materiales(numMat = pNumMat, codigoOmc = registroOMC.Codigo, Consecutivo = ultimoRegistro, descriCorta = cadDescriCorta, descriLarga = cadDescriLarga, Comentarios = request.POST.get('comentarios'), palabrasCve = request.POST.get('palabrasCve'), codigoBimsa = None, fk_Omc23 = registroOMC, fk_Omc41 = None)
            materiales.save()
            #--INSERTAR EN LA TABLA DE CONCRETO
            #cadena2 = 'numMat:' + str(pNumMat) + ',Codigo:' + str(request.POST.get('codigoOmc')) + ',fk_Material:' + ',fk_ClasExpo:' + str(request.POST.get('idClasExpo')) + ',fk_SistColoc:' + str(request.POST.get('idSistColoc')) + ',fk_Densidad:' + str(request.POST.get('idDensidad')) + ',fk_Reven:' + str(request.POST.get('idReven')) + ',fk_FlujoRev:' + str(request.POST.get('idFlujoRev')) + ',fk_FibraConcre:' + str(request.POST.get('idFibraConcre')) + ',fk_ValEsf:' + str(request.POST.get('idValEsf')) + ',fk_Tma:' + str(request.POST.get('idTma')) + ',fk_AplPrinc:' + str(request.POST.get('idAplPrinc'))
            #print(cadena2)
            concreto = Concreto(numMat = pNumMat, Codigo = registroOMC.Codigo, fk_Material = materiales, fk_ClasExpo = registroClasExpo, fk_SistColoc = registroSistColoc, fk_Densidad = registroDensidad, fk_Reven = registroReven, fk_FlujoRev = registroFlujoRev, fk_FibraConcre = registroFibraCon, fk_ValEsf = registroValEsf, fk_Tma = registroTma, fk_AplPrinc = registroAplPrin)
            concreto.save()
            #--INSERTAR EN LA TABLA DE CARACESPE
            #newForm = formCaracEspe.save(commit=False)
            #cadena3 = str(newForm.Acronimo) + '-' + str(newForm.modElast) + '-' + str(newForm.Edad) + '-' + str(newForm.absorcionCap) + '-' + str(newForm.Acronimo2) + '-' + str(newForm.trabaExtend) + '-' + str(newForm.Clase) + '-' + str(newForm.Color) + '-' + str(newForm.Comportamiento) + '-' + str(newForm.conAire) + '-' + str(newForm.conIonClor) + '-' + str(request.POST.get('idIonClor') + '-' + str(newForm.tiempoPrueba))
            #print(cadena3)
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

    return render(request, "ProyectoDemoCostosApp/concreto.html", {'listaOMC': listaOMC, 'registroOMC': registroOMC, 'ultimoRegistro':ultimoRegistro,'formCaracEspe':formCaracEspe,'datEsfuerzo': datEsfuerzo,'datValorEsfuerzo': datValorEsfuerzo, 'datTipoResistencia':datTipoResistencia, 'datAplPrincipales':datAplPrincipales, 'daTma':daTma, 'datRevenimiento':datRevenimiento, 'datDensidad':datDensidad, 'datSisColocacion':datSisColocacion,'datClasExposicion':datClasExposicion,'datFlujoRev':datFlujoRev,'datIonCloruro':datIonCloruro,'datFibraConcre':datFibraConcre,'datUnidadesMedida':datUnidadesMedida})

def ValidaCadena(label, dato, adicion):
    if not dato:
        return ''
    else:
        return label + str(dato).strip() + adicion

def generarConsecutivo(ultimoConsecutivo):
    consecutivoInt = int(ultimoConsecutivo)
    consecutivoInt = consecutivoInt + 1
    consecutivoInt = str(consecutivoInt).rjust(5,'0')
    return str(consecutivoInt)

def listarConcreto(request): #FUNCION QUE SE TRAE TODOS LOs CONCRETOS
    with connection.cursor() as cursor:
        #cursor.execute("SELECT idConcreto, Codigo FROM Concreto")
        cursor.execute("SELECT Materiales.idMaterial,Materiales.numMat,Materiales.codigoOmc AS CodigoOmc23,Omniclass23.descriSpa AS Nombre, acroEsf.Sigla AS siglaVE, ValorEsfuerzo.Valor AS ValorEsfuerzo, uniVal.Unidad AS unidadVal, TipoResistencia.Tipo AS TipoResistencia, acroTma.Sigla AS siglaTma, TMA.valTma, acroRev.Sigla AS siglaRev, Revenimiento.valRev, uniRev.Unidad AS unidadRev, CaracEspe.Clase, SistColocacion.tipoSistema FROM Omniclass23 JOIN  Materiales ON fk_Omc23=idOmc23 JOIN Concreto ON fk_Material=idMaterial JOIN ValorEsfuerzo ON fk_ValEsf=idValEsf JOIN Esfuerzo ON Esfuerzo.idEsfuerzo=ValorEsfuerzo.fk_Esfuerzo JOIN UnidadesMedida uniVal ON uniVal.idUniMed=ValorEsfuerzo.fk_UniMed JOIN Acronimo acroEsf ON Esfuerzo.fk_Acronimo=acroEsf.idAcronimo JOIN TipoResistencia ON idTipoResist=fk_TipoResist JOIN TMA ON fk_Tma=idTma JOIN Acronimo acroTma ON Tma.fk_Acronimo=acroTma.idAcronimo JOIN Revenimiento ON fk_Reven=idReven JOIN Acronimo acroRev ON Revenimiento.fk_Acronimo=acroRev.idAcronimo JOIN UnidadesMedida uniRev ON Revenimiento.fk_UniMed=uniRev.idUniMed JOIN CaracEspe ON fk_Concreto=idConcreto JOIN SistColocacion ON fk_SistColoc=idSistColoc")
        listarConcreto =dictfetchall(cursor)
    #listarConcreto = Concreto.objects.all()

    return render(request, "ProyectoDemoCostosApp/listadoConcreto.html", {"listadoConcreto": listarConcreto})

def dictfetchall(cursor): 
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]