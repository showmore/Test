from django import forms
from django.forms import fields

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'