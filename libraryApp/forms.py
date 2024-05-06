from django import forms
from .models import CartItem, Book_Request

class DocumentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['book'].label = ''

    class Meta:
        model = CartItem
        fields = ["book"]


class BookRequest(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['book_title'].label = ''

    class Meta:
        model = Book_Request
        fields = ["book_title", "book_author"]
