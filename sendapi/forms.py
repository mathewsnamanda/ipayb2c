from django import forms
from django.http import response

class SendapiForm(forms.Form):
    vid=forms.CharField(label='Vid ID')
    reference=forms.CharField(label='Refrence ID')
    phone=forms.CharField(label='Receiver Phone')
    amount=forms.CharField()
   