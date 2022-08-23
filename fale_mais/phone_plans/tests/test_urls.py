from django.urls import resolve, reverse


def test_form_charge_url():
    assert reverse("phone_plans:process_charges") == "/phone_plans/process_charges/"

def test_phone_plans_home_url():
    assert reverse("phone_plans:home") == "/phone_plans/"

def test_name_form_charge_url():
    assert resolve("/phone_plans/process_charges/").view_name == "phone_plans:process_charges"
