from django import forms
from first_app.models import studentModel

class studentForm(forms.ModelForm):
    class Meta:
        model = studentModel
        fields = '__all__'
        # fields = ['roll', 'name', 'father_name']
        # exclude = ['father_name']
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll'
        }
        widgets = {
            'name' : forms.TextInput()
        }
        help_texts = {
            'name': 'write your full name'
        }