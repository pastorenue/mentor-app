from django.apps import AppConfig
from django.db.models.signals import post_migrate
from .signals import handlers


class MenteeConfig(AppConfig):
    name = 'mentee'
    verbose_name = "Mentee"
