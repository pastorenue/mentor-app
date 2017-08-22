from django import forms
from .models import Industry, Expert, Address
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class IndustryForm(forms.ModelForm):

	class Meta:
		model = Industry
		fields = '__all__'


class ExpertSignUpForm(UserCreationForm):
	username = forms.CharField(label=_("Email"), widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'email address e.g example@example.com'}))
	
	def __init__(self, *args, **kwargs):
		super(ExpertSignUpForm, self).__init__(*args, **kwargs)
		self.fields['first_name'].widget.attrs = {'class':'form-control', 'placeholder':'First Name'}

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

class BasicExpertForm(forms.ModelForm):

	class Meta:
		model = Expert
		fields = ('title', 'photo', 'age_range', 'phone_number', 'short_biography')

class ExpertProfessionalForm(forms.ModelForm):

	class Meta:
		model = Expert
		fields = ('industry', 'availability', 'type_to_handle', 'cv_file', 'linkedin_url')

class AddressForm(forms.ModelForm):
	class Meta:
		model = Address
		exclude = ('user',)