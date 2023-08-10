from django import forms
class formname(forms.Form):
    name=forms.CharField(max_length=265)
    password=forms.PasswordInput()
    email=forms.EmailField()