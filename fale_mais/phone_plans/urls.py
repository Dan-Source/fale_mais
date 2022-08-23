from django.urls import path

from fale_mais.phone_plans.views import (
    phone_plans_form_view,
    phone_plans_home_view,
)

app_name = "phone_plans"
urlpatterns = [
    path("", phone_plans_home_view, name="home"),
    path("process_charges/", view=phone_plans_form_view, name="process_charges"),
]
