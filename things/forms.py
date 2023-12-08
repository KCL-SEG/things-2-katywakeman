"""Forms of the project."""
from django import forms
from django.core.validators import RegexValidator
from .models import Thing
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your forms here.

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        labels = {
            'name': 'Name',
            'description': 'Description',
            'quantity': 'Quantity',
        }
        widgets = {
            'description': forms.Textarea(), 'quantity':forms.NumberInput()
        }

    # Additional form-level validation can be defined here if needed.

    # Individual form fields
    name = forms.CharField(max_length=30)
    description = forms.CharField(max_length=120)
    quantity = forms.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(100),
    ])



# class ThingForm(forms.ModelForm):
#     model = Thing
#     name = forms.CharField(label='Name', max_length=30)
#     description = forms.CharField(widget=forms.Textarea(attrs={'name':'description', 'rows':3, 'cols':5}), label ='description',max_length=120)
#     quantity = forms.IntegerField(label='Quantity', validators=[
#             MinValueValidator(0),
#             MaxValueValidator(100),
#         ])
    
    # class Meta:
    #     model = Thing
    #     fields = ['name', 'description', 'quantity']
    #     
    # def clean_quantity(self):
    #     quantity = self.cleaned_data['quantity']

    #     # Add custom validation logic
    #     if quantity < 0:
    #         raise forms.ValidationError('Quantity must be a non-negative number.')
        
    #     if quantity > 100:
    #         raise forms.ValidationError('Quantity must be less than 100.')

    #     return quantity
    
    # def clean_description(self):
    #     description = self.cleaned_data['description']

       
    #     return description
    
    # def clean_name(self):
    #     name = self.cleaned_data['name']

    #     # Add custom validation logic
        

    #     return name