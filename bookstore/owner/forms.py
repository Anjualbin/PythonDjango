from django import forms

class BookForm(forms.Form):
    book_name=forms.CharField()
    author=forms.CharField()
    price=forms.IntegerField()
    copies=forms.IntegerField()

class RegistrationForm(forms.Form):
    firstname=forms.CharField()
    username=forms.CharField()
    email=forms.CharField()
    password1=forms.CharField()
    password2=forms.CharField()

    def clear(self):
        print("validation")
class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()