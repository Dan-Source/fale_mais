import pytest

from fale_mais.users.models import User
from fale_mais.phone_plans.models import PhonePlan, Charge, codeDDD
from fale_mais.users.tests.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()

@pytest.fixture
def phone_plan(db) -> PhonePlan:
    return PhonePlan.objects.create(
        name='FaleMais 30',
        description='Plano de telefone com 30 minutos',
        price=9.90,
        time_limit=30
    )

@pytest.fixture
def charge(db) -> Charge:
    return Charge.objects.create(
        origin=codeDDD.objects.create(code='011', city='São Paulo', state='SP'),
        destiny=codeDDD.objects.create(code='016', city='Campinas', state='SP'),
        tax=0.1
    )
