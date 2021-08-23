from django import forms

class MobileForm(forms.Form):
    mobile_name=forms.CharField()
    model=forms.CharField()
    price=forms.IntegerField()
