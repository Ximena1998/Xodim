from django import forms
from .models import Empleado, Sintomatología

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

class SintomatologiaForm(forms.ModelForm):
    
    class Meta:
        OPTIONS = [
            ('Si', 'SI'),
             ('No', 'NO'),
        ]
        model = Sintomatología
        
        fields = [
            'mucosidad',
            'dolorMuscular',
            'sintGastrointestinal',
            'fechaRegistro',
            'faltaAire',
            'temperatura',
            'tos',
            'contacto',
            'sintCedula',
        ]
        labels = {
            'mucosidad': '¿Tiene mucosidad en la nariz?',
            'dolorMuscular': '¿Tiene dolor muscular?',
            'sintGastrointestinal': '¿Tienes alguna molestía Gastrointestinal?',
            'fechaRegistro': 'Fecha de Registro',
            'faltaAire': '¿Tienes sensación de falta de aire brusco (En ausencia de cualquier otra patología que justifique este síntoma)?',
            'temperatura': '¿Tiene Fiebre?',
            'tos': '¿Tienes tos seca y persitente?',
            'contacto': '¿Has tenido contacto estrecho con algún paciente positivo confirmado?',
            'sintCedula': 'Cédula',
        }
     
        class SimpleForm(forms.Form):
            mucosidad = forms.ChoiceField(
                required=True,
                label='Enter',
                initial='Si',
                disabled='false',
                widget=forms.CheckboxSelectMultiple,
                choices='OPTIONS',
             ) ,
            dolorMuscular= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
                choices='OPTIONS',
             ) ,
            sintGastrointestinal= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
                choices='OPTIONS',
             ) ,
            fechaRegistro= forms.TextInput(attrs = {'class':'form-control'}),
            faltaAire= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
                choices='OPTIONS',
             ) ,
            temperatura= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
                choices='OPTIONS',
             ) ,
            tos= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
                choices='OPTIONS',
             ) ,
            contacto= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
                choices='OPTIONS',
             ) ,
            sintCedula= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
                choices='OPTIONS',
             ) 
        