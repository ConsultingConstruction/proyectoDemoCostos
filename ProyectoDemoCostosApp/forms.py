from django.forms import ModelForm
from ProyectoDemoCostosApp.models import CaracEspe

class CaracEspeForm(ModelForm):
    class Meta:
        model = CaracEspe
        fields = '__all__'

#HACER EL FORM PARA 'PropTermicas'