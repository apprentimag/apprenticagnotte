from django.contrib import admin

from .models import Budget, FinancialContribution

admin.site.register(Budget)
admin.site.register(FinancialContribution)
