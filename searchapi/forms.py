from django import forms
from django.http import response

class SearchapiForm(forms.Form):
    vid=forms.CharField(label='Vid ID')
    reference=forms.CharField(label='Refrence ID')
   