from django import forms

class CervezaFormulario(forms.Form):
    
    estilo = forms.CharField()
    ibu = forms.IntegerField()
    alcohol = forms.IntegerField()
    

class MenuFormulario(forms.Form):
    minutas = forms.CharField()
    descripcion = forms.CharField()
    precio = forms.IntegerField()

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()