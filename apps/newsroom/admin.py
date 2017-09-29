from django.contrib import admin
from .models import *

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
	list_display = ('author', 'title')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('user', 'name')
