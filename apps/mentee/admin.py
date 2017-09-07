from django.contrib import admin
from .models import Mentee, MentorshipRequest

@admin.register(Mentee)
class MenteeAdmin(admin.ModelAdmin):
	list_display = ('name',)

@admin.register(MentorshipRequest)
class MentorshipAdmin(admin.ModelAdmin):
	list_display = ('mentee', 'to_user')