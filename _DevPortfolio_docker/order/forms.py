from order.models import Order
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'email', 'project_description', 'budget', 'deadline']
        widgets = {
            'project_description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'budget': forms.NumberInput(attrs={'class': 'form-control'}),
            'deadline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Наприклад: 2 тижні'}),
        }
