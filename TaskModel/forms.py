from .models import Task
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'assigned_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'category': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'due_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            
        }