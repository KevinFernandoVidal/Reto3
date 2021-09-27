from django.contrib.auth.models import User
from django.forms import fields, widgets
from django import forms
from .models import *

class agregar_moto_form (forms.ModelForm):
    class Meta:
        model = Moto
        fields = '__all__'
        exclude = ['propietario']

class persona_form (forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'
        exclude = ['id_usuario']

class agragar_user_form (forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = []        

class login_form (forms.Form):
    usuario = forms.CharField(widget=forms.TextInput())  
    clave   = forms.CharField(widget=forms.PasswordInput(render_value=False))  

class registro_form (forms.Form):
    correo    = forms.EmailField(label='Ingrese su correo', widget= forms.TextInput(attrs={'class':'form-control'}))
    clave_1  = forms.CharField(label='Ingrese su contraseña', widget= forms.PasswordInput(attrs={'class':'form-control'},render_value= False))
    clave_2  = forms.CharField(label='Confirme la contraseña', widget= forms.PasswordInput(attrs={'class':'form-control'}, render_value= False))

    def clean_username(self):
        correo = self.cleaned_data['correo']
        try:
            c = User.objects.get(username = correo)
        except User.DoesNotExist:
            return correo
        raise forms.ValidationError('El correo ingresado, ya se encuentra registrado')

    
    
    def clean_clave_2 (self):
        clave_1 = self.cleaned_data['clave_1']
        clave_2 = self.cleaned_data['clave_2']
        if clave_1 == clave_2:
            return clave_2
        else:
            raise forms.ValidationError ('las contraseñas no coinciden, por favor Intente nuevamente')


class asignar_moto_form(forms.ModelForm):
    class Meta:
        model = Historial
        fields = '__all__'
        exclude = ['moto']

class traspasar_moto_form(forms.ModelForm):
    class Meta:
        model = Historial
        fields = '__all__'
        exclude = ['moto', 'estado']
         
class mantenimiento_agregar_form(forms.ModelForm):           
    class Meta:
        model = Mantenimientos
        fields = '__all__'
        exclude =['moto', 'responsable']

class mantenimiento_editar_form(forms.ModelForm):           
    class Meta:
        model = Mantenimientos
        fields = '__all__'
        exclude =['moto', 'responsable', 'placa', 'chasis']


        