from django import forms

from .models import Customer, ShippingAddress


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "company_name"
        ]

        widgets = {
            "first_name": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Ваш текст"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Ваш текст"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Ваш текст"
            }),
            "phone_number": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Ваш текст"
            }),
            "company_name": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Ваш текст"
            }),
        }


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = [
            "address_line_1",
            "address_line_2",
            "town",
            "state"
        ]

        widgets = {
            "address_line_1": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "House number and street name"
            }),
            "address_line_2": forms.TextInput(attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Apartment, Suite, Unit, etc (optional)"
            }),
            "town": forms.TextInput(attrs={
                "class": "form-control form-control-lg"
            }),
            "state": forms.TextInput(attrs={
                "class": "form-control form-control-lg"
            })
        }
