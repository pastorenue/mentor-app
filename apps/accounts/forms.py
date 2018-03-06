from django.forms import ModelForm
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
	#Customise the username field to accept email
	username = forms.CharField(label=_("Email"), widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'email address e.g example@example.com'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2')