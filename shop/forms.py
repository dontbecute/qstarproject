# forms.py
from django import forms

class CartAddProductForm(forms.Form):
    # The available quantity choices will be dynamically generated
    quantity = forms.TypedChoiceField(coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        # Pass the available quantity choices when initializing the form
        product = kwargs.pop('product', None)
        super().__init__(*args, **kwargs)
        if product:
            self.fields['quantity'].choices = [(i, str(i)) for i in range(1, product.quantity_available + 1)]
