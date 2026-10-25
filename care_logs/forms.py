from datetime import date

from django import forms
from .models import CareActivity


class CareActivityForm(forms.ModelForm):
    class Meta:
        model = CareActivity
        fields = ['name', 'date', 'description', 'pet']

        labels = {
            'name': 'Дейност',
            'date': 'Дата',
            'description': 'Описание',
            'pet': 'Любимец',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'напр. Ваксина, Храна, Разходка'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Описание...'}),
        }

        error_messages = {
            'name': {
                'required': 'Моля, въведи вида грижа.',
            },
            'pet': {
                'required': 'Избери за кой любимец е грижата.',
            },
        }

    def clean_date(self):
        activity_date = self.cleaned_data['date']
        if activity_date > date.today():
            raise forms.ValidationError('Датата не може да е в бъдещето.')
        return activity_date