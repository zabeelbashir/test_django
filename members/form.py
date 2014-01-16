'''
Created on Jan 16, 2014

@author: zabeel
'''
from django import forms
class NameForm(forms.Form):
    name = forms.CharField()
    def getName(self):
        return self.cleaned_data["name"]
    def clean_name(self):
        name = self.cleaned_data.get("name","")
        if len(name) < 3:
            raise forms.ValidationError("Name should be at least 3 characters long")
        return name