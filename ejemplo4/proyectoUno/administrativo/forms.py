from django.forms import ModelForm
from administrativo.models import Estudiante, Pais


class EstudianteForm(ModelForm): 
    class Meta:
        model = Estudiante 
        fields = ['nombre', 'apellido', 'cedula'] 

class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = ['p_nombre', 'p_capital', 'num_provincias', 'num_habitantes']
        

