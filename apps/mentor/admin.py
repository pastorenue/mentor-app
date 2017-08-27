from django.contrib import admin
from .models import Mentor 
# Register your models here.
@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
	list_display = ('name',)