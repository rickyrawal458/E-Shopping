from django import forms
from .models import Order
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address','postal_code', 'city']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','width': 10,'style': 'background-color: #cfcccc85;'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','style': 'background-color: #cfcccc85;'}),
            'email': forms.TextInput(attrs={'class': 'form-control','style': 'background-color: #cfcccc85;'}),
            'address': forms.TextInput(attrs={'class': 'form-control','style': 'background-color: #cfcccc85;'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control','style': 'background-color: #cfcccc85;'}),
            'city': forms.TextInput(attrs={'class': 'form-control','style': 'background-color: #cfcccc85;'}),
        }