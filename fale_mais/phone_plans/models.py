from django.db import models


class codeDDD(models.Model):

    code = models.CharField(max_length=3)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.city} - {self.state} ({self.code})'

    class Meta:
        verbose_name = 'DDD'
        verbose_name_plural = 'DDDs'

class Charge(models.Model):
    origin = models.ForeignKey(
        codeDDD,
        on_delete=models.CASCADE,
        related_name='origin'
    )

    destiny = models.ForeignKey(
        codeDDD,
        on_delete=models.CASCADE,
        related_name='destiny'
    )
    tax = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.origin} - {self.destiny} ({self.tax})'

class PhonePlan(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    time_limit = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Plano de Telefone'
        verbose_name_plural = 'Planos de Telefone'
