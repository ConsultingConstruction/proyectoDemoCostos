from django.urls import path

from ProyectoDemoCostosApp import views

urlpatterns = [
    path('', views.principal, name="Principal"),
    path('nivel/<int:bandera>/<int:aux_nivel>', views.obtenerNivelEspecifico, name="Nivel"),
    path('material/<int:idOmc>/<int:numMat>', views.obtenerMaterial, name="Material"),
    path('material/listarConcreto', views.listarConcreto, name="listarConcreto")
    

]