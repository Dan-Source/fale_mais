from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PhonePlansConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "fale_mais.phone_plans"
    verbose_name = _("Phone Plans")
