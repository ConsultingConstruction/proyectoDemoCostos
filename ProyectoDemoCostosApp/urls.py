from django.urls import path

from ProyectoDemoCostosApp import views

urlpatterns = [
    path('', views.principal, name="Principal"),
    path('nivel/<int:aux_nivel>', views.obtenerNivelEspecifico, name="Nivel")

]