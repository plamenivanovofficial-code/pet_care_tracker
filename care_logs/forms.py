from django import forms
from .models import CareActivity

class CareActivityForm(forms .ModelForm):
    class Meta: 
        model = CareActivity
        fields = ['title', 'date' , 'notes' , 'pets']
        
