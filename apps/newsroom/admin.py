from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *
from django.template.defaultfilters import slugify


@admin.register(Entry)
class EntryAdmin(SummernoteModelAdmin):
	fields = ('author','title','content')
	

	def save_model(self, request, obj, form, change):
		obj.slug = slugify(obj.title)
		super(EntryAdmin, self).save_model(request, obj, form, change)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('user', 'name')
