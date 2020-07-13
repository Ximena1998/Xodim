from django import forms
from .models import Empleado, Sintomatología,horario

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
"""
class presentacionForm(forms.ModelForm):
    class Meta:
        model = presentacion
        fields = '__all__'
"""
class SintomatologiaForm(forms.ModelForm):
    
    class Meta:
       
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
            'faltaAire': '¿Tienes sensación de falta de aire brusco ?',
            'temperatura': '¿Tiene Fiebre?',
            'tos': '¿Tienes tos seca y persitente?',
            'contacto': '¿Has tenido contacto estrecho con algún paciente positivo confirmado?',
            'sintCedula': 'Cédula: ',
        }
     
        class SimpleForm(forms.Form):
            mucosidad = forms.IntegerField(label='Multiplex level ',required=False, widget=forms.TextInput()),
            dolorMuscular= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
             ) ,
            sintGastrointestinal= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
             ) ,
            fechaRegistro= forms.TextInput(attrs = {'class':'form-control'}),
            faltaAire= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
             ) ,
            temperatura= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
             ) ,
            tos= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
             ) ,
            contacto= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
             ) ,
            sintCedula= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
             ) 
        
class horarioForm (forms.ModelForm):
     class Meta:
        model = horario
        fields = [
            'idHorario',
            'fechaRegistro',
            'horaEntradaM',
            'horaSalidaM',
            'horaEntradaV',
            'horaSalidaV',
            'horasExtra',
            'sintCedula',

        ]
        labels = {
            'fechaRegistro' : 'Fecha: ',
            'horaEntradaM': 'Hora Matutina de Entrada: ',
            'horaSalidaM': 'Hora Matutina de Salida: ',
            'horaEntradaV': 'Hora Vespertina de Entrada: ',
            'horaSalidaV': 'Hora Vespertina de Salida: ',
            'horasExtra': 'Horas Extra: ',
            'sintCedula': 'Cédula',
        }
        class SimpleForm(forms.Form):
            fechaRegistro= forms.TextInput(attrs = {'class':'form-control'}),
            horaEntradaM= forms.TextInput(attrs = {'class':'form-control'}),
            horaSalidaM= forms.TextInput(attrs = {'class':'form-control'}),
            horaEntradaV= forms.TextInput(attrs = {'class':'form-control'}),
            horaSalidaV= forms.TextInput(attrs = {'class':'form-control'}),
            horasExtra= forms.TextInput(attrs = {'class':'form-control'}),
            sintCedula= forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
             ) 