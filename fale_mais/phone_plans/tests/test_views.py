import pytest
from fale_mais.phone_plans.forms import FormCharge
from fale_mais.phone_plans.models import PhonePlan, Charge

pytestmark = pytest.mark.django_db


class TestPhonePlansFormView:

    def form_is_valid(self, phone_plan: PhonePlan, charge: Charge):
        form = FormCharge(
            data={
                'charge': charge.id,
                'phone_plan': phone_plan.id,
                'minutes': 1,
            }
        )

        assert form.is_valid()
        assert form.cleaned_data['charge'] == charge
        assert form.cleaned_data['phone_plan'] == phone_plan
        assert form.cleaned_data['minutes'] == 1

    def test_form_response(self, phone_plan: PhonePlan, charge: Charge):
        """
        Test form response.
        """

        form = FormCharge(
            data={
                'charge': charge.id,
                'phone_plan': phone_plan.id,
                'minutes': 31,
            }
        )

        assert form.is_valid()
        assert form.cleaned_data['charge'] == charge
        assert form.cleaned_data['phone_plan'] == phone_plan
        assert form.cleaned_data['minutes'] == 31
