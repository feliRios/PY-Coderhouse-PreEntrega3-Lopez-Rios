from django import forms


class SearchProduct(forms.Form):
    nombre = forms.CharField()