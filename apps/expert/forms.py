from django import forms
from .models import Industry, Expert, Address
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class IndustryForm(forms.ModelForm):

	class Meta:
		model = Industry
		fields = '__all__'

class ExpertForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ExpertForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs = {'class':'form-control'}
		self.fields['name'].widget.attrs = {'class':'form-control'}
		self.fields['age_range'].widget.attrs = {'class':'form-control'}
		self.fields['industry'].widget.attrs = {'class':'form-control'}
		self.fields['availability'].widget.attrs = {'class':'form-control'}
		self.fields['phone_number'].widget.attrs = {'class':'form-control'}
		self.fields['type_to_handle'].widget.attrs = {'class':'form-control'}
		self.fields['short_biography'].widget.attrs = {'class':'form-control'}
		self.fields['photo'].widget.attrs = {'class':'form-control'}
		self.fields['cv_file'].widget.attrs = {'class':'form-control'}
		self.fields['background_image'].widget.attrs = {'class':'form-control'}
		self.fields['linkedin_url'].widget.attrs = {'class':'form-control'}

	class Meta:
		model=Expert
		exclude = ('user', 'slug', 'email')

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

	def __init__(self, *args, **kwargs):
		super(AddressForm, self).__init__(*args, **kwargs)
		self.fields['street'].widget.attrs = {'class':'form-control'}
		self.fields['city'].widget.attrs = {'class':'form-control'}
		self.fields['state'].widget.attrs = {'class':'form-control'}
		self.fields['country'].widget.attrs = {'class':'form-control'}


	class Meta:
		model = Address
		exclude = ('user',)