from django.apps import AppConfig

# from here we write pagesConfig in second step
class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
