# travel/forms.py

from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password != password_confirm:
            raise forms.ValidationError('Passwords do not match.')

        return cleaned_data
from django.db import models

class BookingForm(models.Model):  
    hotel_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.hotel_name}"


