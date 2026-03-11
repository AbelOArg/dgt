from django import forms
from .models import empleado

class empleadoForm(forms.ModelForm):
    class Meta:
        model = empleado
        fields = '__all__'