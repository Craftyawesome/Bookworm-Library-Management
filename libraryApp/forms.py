from django import forms
from .models import CartItem

class DocumentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].label = ''

    class Meta:
        model = CartItem
        fields = ["book"]
