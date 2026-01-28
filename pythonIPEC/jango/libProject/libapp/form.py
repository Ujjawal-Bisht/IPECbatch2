from .models import Book
from django import forms 

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = ["titlt", "auther"]
        fields = '__all__'
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}),
            # 'title' : form.
        }