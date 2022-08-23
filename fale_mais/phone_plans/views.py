from pipes import Template
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from fale_mais.phone_plans.forms import FormCharge

from fale_mais.phone_plans.models import PhonePlan


class PhonePlansHomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['plans'] = PhonePlan.objects.all()
        return context

class PhonePlansFormView(FormView):
    template_name= 'phone_plans/phone_plans_form.html'
    form_class = FormCharge

    def form_valid(self, form):
        if form.is_valid():
            result = form.calculate_phone_plan_charge()
            return render(self.request, 'phone_plans/phone_plans_form.html', {'form': form, 'result': result})


phone_plans_form_view = PhonePlansFormView.as_view()
phone_plans_home_view = PhonePlansHomeView.as_view()
