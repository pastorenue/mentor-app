from django.contrib import admin
from .models import *
from django.template.defaultfilters import slugify


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
	list_display = ('author', 'title')

	def save_model(self, request, obj, form, change):
		obj.slug = slugify(obj.title)
		super(EntryAdmin, self).save_model(request, obj, form, change)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('user', 'name')
