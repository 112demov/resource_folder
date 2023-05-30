from django.apps import AppConfig


class LkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lk'
    
    def ready(self):
        import lk.signals
