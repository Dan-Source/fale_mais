

from decimal import Decimal
from typing import Any
from fale_mais.phone_plans.utils.constants import ADDITIONAL_PERCENTAGE


class ProcessPhonePlansCharges():
    """
        Calculates charges on calls according to registered plans.
    """

    def __init__(self, phone_plan: object, charge: object):
        self.phone_plan = phone_plan
        self.charge = charge

    def format_numbers(self, number: Any) -> str:
        """
            Formats a number to have only two decimals.
            params: number to be formatted.
            return: formatted number.
        """

        return Decimal(number).quantize(Decimal('1.00'))

    def get_normal_charge(self, time) -> dict:
        """
            Calculates the charge of a call without plan.

            params: time of the call in minutes.
            return: A dict with the charge details.
        """

        charge_tax = float(self.charge.tax)
        total = time * charge_tax
        total = self.format_numbers(total)

        return total

    def calculate_charge(self, time: int) -> dict:
        """
            Calculates the charge of a call.

            params: time of the call in minutes.
            return: A dict with the charge details.
        """

        if time <= self.phone_plan.time_limit:
            return {
                'plan': self.phone_plan,
                'charge': self.charge,
                'tax': 0,
                'total': 0,
                'total_without_plan': self.get_normal_charge(time),
            }

        exceeded_time = time - self.phone_plan.time_limit

        if exceeded_time > 0:
            charge_tax = float(self.charge.tax)
            additional_charge_tax = charge_tax * (ADDITIONAL_PERCENTAGE / 100)
            tax = charge_tax + additional_charge_tax
            total = exceeded_time * tax
            total = self.format_numbers(total)
            return {
                'plan': self.phone_plan,
                'charge': self.charge,
                'tax': self.format_numbers(tax),
                'total': total,
                'total_without_plan': self.get_normal_charge(time),
            }
