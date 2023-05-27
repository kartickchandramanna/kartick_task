from django import forms
from .models import Customer, Car, Address


MODEL_CHOICES = (
        ('model1', 'Model 1'),
        ('model2', 'Model 2'),
        ('model3', 'Model 3'),
    )
MANUFACTURER_CHOICES = (
        ('manufacturer1', 'Manufacturer 1'),
        ('manufacturer2', 'Manufacturer 2'),
        ('manufacturer3', 'Manufacturer 3'),
    )
COLOR_CHOICES = (
        ('color1', 'Color 1'),
        ('color2', 'Color 2'),
        ('color3', 'Color 3'),
    )


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_name','pincode','city','state','country_code']
        widgets = {
            'street_name':forms.TextInput(attrs={'class':'form-control'}),
            'pincode':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.TextInput(attrs={'class':'form-control'}),
            'country_code':forms.TextInput(attrs={'class':'form-control'}),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','last_name','age','date_of_birth','phone','email']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['model_name','manufacturing_date','manufacturer','color']
        widgets = {
            'model_name': forms.Select(choices=MODEL_CHOICES, attrs={'class':'form-control'}),
            'manufacturing_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class':'form-control'}),
            'manufacturer': forms.Select(choices=MANUFACTURER_CHOICES, attrs={'class':'form-control'}),
            'color': forms.Select(choices=COLOR_CHOICES, attrs={'class':'form-control'}),
        }


# class StudentRegistration(forms.ModelForm):
    
#     class Meta:
#         model = User
#         fields = ['name','email','password']
#         widgets={
#             'name':forms.TextInput(attrs={'class':'form-control','id':'my_fucking'}),
#             'email':forms.EmailInput(attrs={'class':'form-control'}),
#             'password':forms.PasswordInput(attrs={'class':'form-control'}),
#         }