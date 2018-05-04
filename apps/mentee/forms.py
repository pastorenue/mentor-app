from django import forms 
from .models import Mentee
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _


class BasicMenteeForm(forms.ModelForm):

	class Meta:
		model = Mentee
		fields = ('title', 'photo', 'age_range', 'phone_number',)


class MenteeForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(MenteeForm, self).__init__(*args, **kwargs)
		self.fields['title'].widget.attrs = {'class':'form-control'}
		self.fields['name'].widget.attrs = {'class':'form-control'}
		self.fields['age_range'].widget.attrs = {'class':'form-control'}
		self.fields['industry'].widget.attrs = {'class':'form-control'}
		self.fields['specify_industry'].widget.attrs = {'class':'form-control'}
		self.fields['phone_number'].widget.attrs = {'class':'form-control'}
		self.fields['year_of_commencement'].widget.attrs = {'class':'form-control'}
		self.fields['time_with_mentor'].widget.attrs = {'class':'form-control'}
		self.fields['phone_number'].widget.attrs = {'class':'form-control'}
		self.fields['photo'].widget.attrs = {'class':'form-control'}
		self.fields['name_of_business'].widget.attrs = {'class':'form-control'}
		self.fields['mode_of_communication'].widget.attrs = {'class':'form-control'}
		self.fields['mode_details'].widget.attrs = {'class':'form-control'}
		self.fields['level_of_education'].widget.attrs = {'class':'form-control'}
		self.fields['background_image'].widget.attrs = {'class':'form-control'}

	class Meta:
		model = Mentee
		exclude = ('user', 'email', 'slug', 'address')
class MenteeProfessionalForm(forms.ModelForm):

	class Meta:
		model = Mentee
		fields = ('level_of_education', 'name_of_business', 'industry', 'year_of_commencement', 'time_with_mentor', 'mode_of_communication', 'mode_details')


class MenteeSignUpForm(UserCreationForm):
	username = forms.CharField(label=_("Email"), widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'email address e.g example@example.com'}))

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'password1', 'password2')