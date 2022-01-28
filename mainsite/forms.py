from django import forms


class ContactForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField()

