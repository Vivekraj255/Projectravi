from django import forms
from .models import Update

class UpdateForm(forms.ModelForm):

    class Meta:
        model = Update
        fields = ["title", "cover"]