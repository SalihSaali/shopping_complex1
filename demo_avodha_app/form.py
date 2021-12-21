from.models import shop
from django import forms

class Modelform(forms.ModelForm):
    class Meta:
        model=shop
        fields=['name','desc','img','price']



