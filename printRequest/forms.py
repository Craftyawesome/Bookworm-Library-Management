from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cover'].label = ''

    class Meta:
        model = Document
        fields = ["cover"]
