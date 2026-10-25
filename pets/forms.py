from django import forms
from .models import Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'category', 'age', 'photo_url', 'photo_file', 'description', 'tags']
        labels =  {
            'name': 'Име',
            'category': 'Вид',
            'age': 'Възраст (години)',
            'photo_url': 'Линк към снимка',
            'photo_file': 'Или качи снимка',
            'description': 'Описание',
            'tags': 'Етикети',
        }
        
        widgets = {
            'name': forms.TextInput(attrs= {'placeholder': 'напр. Рекс'}),
            'category': forms.TextInput(attrs={'placeholder': 'напр. Куче, Котка, Папагал'}),
            'photo_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
            'photo_file': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder':'Характер, навици, здраве ...' }),
            'tags': forms.CheckboxSelectMultiple(),
        }
        
        help_texts = {
            'photo_url': 'Постави линк към снимка от интернет.',
            'photo_file': '... или качи снимка от компютъра/телефона си.',
            'tags': 'Избери етикети, ако има такива.',
        }
        
        error_messages = {
            'name': {
                'required': 'Моля, въведи име на любимеца.',
                'max_length': 'Името е твърде дълго (макс. 30 символа).',
            },
        }
        
    def clean_age(self):
        age = self.cleaned_data['age']
        if age > 50:
            raise forms.ValidationError('Любимецът не може да е на повече от 50 години') 
        return age
    
    def clean_category(self):
        category = self.cleaned_data['category']
        category = category.strip().capitalize()
        return category
    
    def clean(self):
        self.cleaned_data = super().clean() 
        photo_url = self.cleaned_data.get('photo_url')
        photo_file = self.cleaned_data.get('photo_file')
        
        if not photo_url and not photo_file:
            raise forms.ValidationError('Добави снимка')  
        return self.cleaned_data  