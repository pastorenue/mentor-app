from django import forms
from .models import Mentor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class MentorForm(forms.ModelForm):

	class Meta:
		model = Mentor
		exclude = ('user',)

class BasicMentorForm(forms.ModelForm):

	class Meta:
		model = Mentor
		fields = ('title', 'photo', 'age_range', 'phone_number', 'short_biography')


class MentorProfessionalForm(forms.ModelForm):

	class Meta:
		model = Mentor
		fields = ('industry', 'years_of_experience', 
					'availability', 'type_to_handle', 
					'cv_file', 'linkedin_url')


class MentorSignUpForm(UserCreationForm):
	username = forms.CharField(label=_("Email"), widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'email address e.g example@example.com'}))

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'password1', 'password2')