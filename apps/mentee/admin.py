from django.contrib import admin
from .models import Mentee

@admin.register(Mentee)
class MenteeAdmin(admin.ModelAdmin):
	list_display = ('name',)
