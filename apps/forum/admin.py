from django.contrib import admin
from .models import Channels

@admin.register(Channels)
class ChannelsAdmin(admin.ModelAdmin):
	list_display = ('name',)
