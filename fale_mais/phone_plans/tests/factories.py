from factory import Faker, post_generation
from factory.django import DjangoModelFactory
from fale_mais.phone_plans.models import codeDDD, Charge, PhonePlan


class codeDDDFactory(DjangoModelFactory):

    class Meta:
        model = codeDDD

    code = Faker("pyint", min_value=1, max_value=99)
    name = Faker("name")

    @post_generation
    def __str__(self):
        return self.code


class ChargeFactory(DjangoModelFactory):

        class Meta:
            model = Charge

        origin = Faker("pyint", min_value=1, max_value=99)
        destiny = Faker("pyint", min_value=1, max_value=99)
        tax = Faker("pyint", min_value=1, max_value=99)

        @post_generation
        def __str__(self):
            return f'{self.origin} - {self.destiny}'


class PhonePlanFactory(DjangoModelFactory):

        class Meta:
            model = PhonePlan

        name = Faker("name")
        description = Faker("text")
        price = Faker("pyint", min_value=1, max_value=99)
        time_limit = Faker("pyint", min_value=1, max_value=99)

        @post_generation
        def __str__(self):
            return self.name
