from django import forms
from fale_mais.phone_plans.utils.process_phone_plans_charges import ProcessPhonePlansCharges
from fale_mais.phone_plans.models import PhonePlan, Charge


class FormCharge(forms.Form):

    charge = forms.ModelChoiceField(queryset=Charge.objects.all())
    phone_plan = forms.ModelChoiceField(queryset=PhonePlan.objects.all())
    minutes = forms.IntegerField(label='Minutos', min_value=1)

    def calculate_phone_plan_charge(self):
        charge = self.cleaned_data['charge']
        phone_plan = self.cleaned_data['phone_plan']
        minutes = self.cleaned_data['minutes']
        process = ProcessPhonePlansCharges(charge=charge, phone_plan=phone_plan)
        response = process.calculate_charge(time=minutes)
        return response
