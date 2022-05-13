from django.apps import AppConfig


class SalesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'backend.sales.app'
    verbose_name = 'sales'
    label = 'sales'
