from django import forms
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['project_title', 'service_type', 'location', 'description']
        widgets = {
            'project_title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Broken Excavator Arm, Tank Fabrication...'
            }),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Dar es Salaam, Mbeya, Arusha, or specific site address...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5,
                'placeholder': 'Describe the problem in detail...'
            }),
        }
        labels = {
            'project_title': 'Project Title',
            'service_type': 'Service Type',
            'location': '📍 Location (Where is the problem?)',
            'description': 'Description',
        }