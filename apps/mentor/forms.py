from django import forms
from .models import Mentor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class MentorForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(MentorForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs = {'class':'form-control'}
		self.fields['age_range'].widget.attrs = {'class':'form-control'}
		self.fields['photo'].widget.attrs = {'class':'form-control'}
		self.fields['phone_number'].widget.attrs = {'class':'form-control'}
		self.fields['short_biography'].widget.attrs = {'class':'form-control'}
		self.fields['availability'].widget.attrs = {'class':'form-control'}
		self.fields['years_of_experience'].widget.attrs = {'class':'form-control'}
		self.fields['type_to_handle'].widget.attrs = {'class':'form-control'}
		self.fields['cv_file'].widget.attrs = {'class':'form-control'}
		self.fields['linkedin_url'].widget.attrs = {'class':'form-control'}
		self.fields['industry'].widget.attrs = {'class':'form-control'}
		self.fields['email'].widget.attrs = {'class':'form-control'}
		self.fields['name'].widget.attrs = {'class':'form-control'}
		self.fields['background_image'].widget.attrs = {'class':'form-control'}

	class Meta:
		model = Mentor
		exclude = ('user', 'slug', 'account_status')

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