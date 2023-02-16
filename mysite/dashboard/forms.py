from django import forms
from .models import Product_selling_price, Product

class Product_selling_priceForm(forms.ModelForm):

    # year = forms.DateField(widget=forms.DateInput(attrs={
    #     'class': 'form-control datepicker-input',
    #     'data-target': '#datepicker1'
    # }))

    class Meta:
        model = Product_selling_price
        fields = "__all__"
        widgets = {
            'year': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            )
        }

class Dashboard_Table_month_basicForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

