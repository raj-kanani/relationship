from django.apps import AppConfig


class RelationappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationapp'

    # def ready(self):
    #         from .import signals