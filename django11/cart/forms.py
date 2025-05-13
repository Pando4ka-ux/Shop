from django import forms
PRODUCT_QUANTITY_CHOICES = [(i, str(i))for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,
        widget=forms.Select(attrs={
            'size': '3', 
            'class': 'my-custom-class',
            'style': 'width:200px;'
        }))

    update = forms.BooleanField(
        required=False, 
        initial=False, 
        widget=forms.HiddenInput()
    )