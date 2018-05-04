from django import forms
from .models import Entry
from django_summernote.widgets import SummernoteWidget

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        widgets = {
            'content': SummernoteWidget(),
        }