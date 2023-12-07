"""Forms of the project."""
from django import forms
from django.core.validators import RegexValidator
from .models import Thing
# Create your forms here.

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['quantity']
        
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']

        # Add custom validation logic
        if quantity < 0:
            raise forms.ValidationError('Quantity must be a non-negative number.')
        
        if quantity > 100:
            raise forms.ValidationError('Quantity must be less than 100.')

        return quantity
    
    def clean_description(self):
        description = self.cleaned_data['description']

       
        return description
    
    def clean_name(self):
        name = self.cleaned_data['name']

        # Add custom validation logic
        

        return name