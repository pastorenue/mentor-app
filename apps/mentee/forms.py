from django import forms 
from .models import Mentee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


class BasicMenteeForm(forms.ModelForm):

	class Meta:
		model = Mentee
		fields = ('title', 'photo', 'age_range', 'phone_number',)


class MenteeProfessionalForm(forms.ModelForm):

	class Meta:
		model = Mentee
		fields = ('level_of_education', 'name_of_business', 'industry', 'year_of_commencement', 'time_with_mentor', 'mode_of_communication', 'mode_details')


class MenteeSignUpForm(UserCreationForm):
	username = forms.CharField(label=_("Email"), widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'email address e.g example@example.com'}))

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'password1', 'password2')