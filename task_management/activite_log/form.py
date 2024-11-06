from django import forms
from .models import ActiviteLog

class ActiviteLogForm(forms.ModelForm):
    class Meta:
        model = ActiviteLog
        fields = ["user", "action"]