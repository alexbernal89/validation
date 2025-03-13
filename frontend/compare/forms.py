from django import forms

class UploadImageForm(forms.Form):
    reference = forms.ImageField(label='Imagen de Referencia')
    target = forms.ImageField(label='Imagen a Comparar')