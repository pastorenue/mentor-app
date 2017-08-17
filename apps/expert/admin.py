from django.contrib import admin
from .models import Industry

# Register your models here.
class IndustryAdmin(admin.ModelAdmin):

	class Meta:
		list_display = ('name',)

admin.site.register(Industry, IndustryAdmin)