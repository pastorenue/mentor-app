from django.contrib import admin
from .models import Industry, Expert

# Register your models here.
class IndustryAdmin(admin.ModelAdmin):

	class Meta:
		list_display = ('name',)

admin.site.register(Industry, IndustryAdmin)

@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):

	class Meta:
		list_display = ('name',)