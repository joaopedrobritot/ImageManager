from django import forms
from .models import Calculator

class CalculatorForm(forms.ModelForm):

    class Meta:
        model = Calculator
        fields = ('your_resin', 'target_resin')
        labels = {
            "your_resin": "Insert your current resin(MAX: 160): ",
            "target_resin": "Insert the target resin(MAX: 160): "
        }