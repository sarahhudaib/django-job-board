from django import forms
from .models import Info


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = '__all__'

