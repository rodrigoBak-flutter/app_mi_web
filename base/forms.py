from django import forms

class FormContact(forms.Form):
    issue=forms.CharField()
    email=forms.EmailField()
    message=forms.CharField()