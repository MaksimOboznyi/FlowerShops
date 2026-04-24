from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone', 'address', 'delivery_time']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'order__form_input',
                'placeholder': 'Введите Имя',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'order__form_input',
                'placeholder': '+ 7 (999) 000 00 00',
            }),
            'address': forms.TextInput(attrs={
                'class': 'order__form_input',
                'placeholder': 'Адрес доставки',
            }),
            'delivery_time': forms.RadioSelect(),
        }
