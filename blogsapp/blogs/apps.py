from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BlogsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blogsapp.blogs"
    verbose_name = _("Users")

    def ready(self):
        try:
            import blogsapp.blogs.signals  # noqa F401
        except ImportError:
            pass
