from django import forms
from .models import *

class Addrooms(forms.ModelForm):
    class Meta:
        model=Rooms
        fields='__all__'
        exclude=['user','created_date']
        widgets = {
            'ammenities': forms.CheckboxSelectMultiple(),  # Or use forms.SelectMultiple()
        }
        


class Addeatery(forms.ModelForm):
    class Meta:
        model=Eatery
        fields='__all__'
        exclude=['user','created_date']

