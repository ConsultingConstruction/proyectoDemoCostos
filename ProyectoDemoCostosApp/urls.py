from django.urls import path

from ProyectoDemoCostosApp import views

urlpatterns = [
    path('', views.principal, name="Principal")

]