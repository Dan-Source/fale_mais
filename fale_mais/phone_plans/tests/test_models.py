from fale_mais.phone_plans.models import PhonePlan, Charge, codeDDD

class TestePhonePlan:
    def test_name_plan(self, phone_plan: PhonePlan):
        phone_plan = PhonePlan(name='FaleMais 30', description='Plano de telefone com 30 minutos', price=9.90, time_limit=30)
        assert str(phone_plan) == 'FaleMais 30'


class TesteCharge:
    def test_name_charge(self, charge: Charge):
        charge = Charge(origin=codeDDD.objects.get(code='011'), destiny=codeDDD.objects.get(code='016'), tax=0.40)
        assert str(charge) == 'São Paulo - SP (011) - Campinas - SP (016) (0.4)'
