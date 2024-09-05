from django import forms
from .models import NearMiss

class NearMissForm(forms.ModelForm):
    class Meta:
        model = NearMiss
        fields = ['title', 'description', 'encounters', 'prevention']
