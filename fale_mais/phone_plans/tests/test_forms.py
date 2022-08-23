"""
    Test Forms for the Phone Plans app.
"""
from decimal import Decimal
from fale_mais.phone_plans.forms import FormCharge
from fale_mais.phone_plans.models import PhonePlan, Charge


class TestFormCharge:
    """
        Test Forms for the Phone Plans app.
    """

    def test_validation_error(self, phone_plan: PhonePlan, charge: Charge):
        """
            Test validation error.
        """
        form = FormCharge(
            data={
                'charge': None,
                'phone_plan': phone_plan.id,
                'minutes': 1,
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "charge" in form.errors
        assert form.errors["charge"][0] == "This field is required."

    def test_validation_success(self, phone_plan: PhonePlan, charge: Charge):
        """
            Test validation success.
        """

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

        data = {
            'plan': phone_plan,
            'charge': charge,
            'tax': Decimal('0.11'),
            'total_without_plan': Decimal('3.10'),
            'total': Decimal('0.11'),
        }

        assert form.is_valid()
        assert form.calculate_phone_plan_charge() == data
