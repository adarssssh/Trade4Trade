from django import forms
from .models import Books
  
class HotelForm(forms.ModelForm):
  
    class Meta:
        model = Books
        fields = ['title', 'price', 'tags', 'category', 'discription', 'image']