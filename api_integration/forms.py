from django import forms

class PacienteRegistroForm(forms.Form):
    rut = forms.CharField(label='RUT')
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    edad = forms.IntegerField(label='Edad')
    email = forms.EmailField(label='Email')
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    
class MedicoRegistroForm(forms.Form):
    rut = forms.CharField(label='RUT')
    nombre = forms.CharField(label='Nombre')
    apellido = forms.CharField(label='Apellido')
    edad = forms.IntegerField(label='Edad')
    especialidad = forms.CharField(label='Especialidad')
    email = forms.EmailField(label='Email')
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    
class ReservaCitaForm(forms.Form):
    paciente_id = forms.IntegerField()
    medico_id = forms.IntegerField()
    fecha_hora = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
