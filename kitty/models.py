from django.utils.crypto import get_random_string
from django.db import models


def generate_token():
    return get_random_string(length=16)


class Budget(models.Model):
    id = models.CharField(max_length=16, primary_key=True, default=generate_token)
    admin_token = models.CharField(max_length=16, default=generate_token)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def total_contributions(self):
        total = 0
        for contribution in self.financialcontribution_set.all():
            total += contribution.amount
        return total

    def __str__(self):
        return self.name


class FinancialContribution(models.Model):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    contributor = models.CharField(max_length=200)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return '{} € ({})'.format(self.amount, self.contributor)
