from django import forms


class SearchProduct(forms.Form):
    nombre = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Nombre del producto'}))
    
    
class RegisterClient(forms.Form):
    nombre = forms.CharField(max_length=30)
    direccion = forms.CharField(max_length=50)
    email = forms.EmailField()
    telefono = forms.IntegerField()
    

class RegisterOrder(forms.Form):
    numero = forms.IntegerField()
    fecha = forms.DateField()
    entregado = forms.BooleanField(required=False)


class ContactForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    asunto = forms.CharField()
    mensaje = forms.CharField(widget=forms.Textarea)
    