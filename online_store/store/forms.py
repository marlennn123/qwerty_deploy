from django import forms
from .models import Product


class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'category', 'description', 'price', 'active', 'date']