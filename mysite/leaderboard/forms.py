from django import forms
from .models import Leader

class LeaderForm(forms.ModelForm):

    class Meta:
        model = Leader
        fields = ['points']