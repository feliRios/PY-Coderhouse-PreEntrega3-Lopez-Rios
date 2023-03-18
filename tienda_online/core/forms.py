from django import forms


class SearchProduct(forms.Form):
    nombre = forms.CharField(max_length=30)
    
    
class RegisterClient(forms.Form):
    nombre = forms.CharField(max_length=30)
    direccion = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField()