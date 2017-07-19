from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Budget, FinancialContribution


class BudgetListView(generic.ListView):
    def get_queryset(self):
        return Budget.objects.order_by('name')[:5]


class BudgetDetailView(generic.DetailView):
    model = Budget


class BudgetAdminDetailView(generic.DetailView):
    model = Budget
    template_name = 'kitty/budget_admin_detail.html'

    def dispatch(self, request, *args, **kwargs):
        object = self.get_object()
        admin_token = kwargs.get('admin_token')
        if object.admin_token != admin_token:
            return HttpResponseForbidden()
        return super(BudgetAdminDetailView, self).dispatch(request, *args, **kwargs)


def budget_create(request):
    budget = Budget(name=request.POST['name'])
    budget.save()
    return HttpResponseRedirect(reverse(
        'kitty:budget/admin/detail',
        args=(budget.id, budget.admin_token,)
    ))


def budget_admin_update(request, pk, admin_token):
    budget = get_object_or_404(Budget, pk=pk)
    if budget.admin_token != admin_token:
        return HttpResponseForbidden()

    budget.name = request.POST['name']
    budget.description = request.POST['description']
    budget.save()

    return HttpResponseRedirect(reverse(
        'kitty:budget/admin/detail',
        args=(budget.id, budget.admin_token,)
    ))


def financial_contribution_create(request, budget_id):
    budget = get_object_or_404(Budget, pk=budget_id)
    try:
        budget.financialcontribution_set.create(
            amount=request.POST['amount'],
            contributor=request.POST['contributor'],
        )
    except ValueError:
        return render(request, 'kitty/budget_detail.html', {
            'budget': budget,
            'error_message': 'Le montant doit être un nombre',
        })
    return HttpResponseRedirect(reverse('kitty:budget/detail', args=(budget.id,)))


def financial_contribution_admin_confirm(request, pk, admin_token):
    contribution = get_object_or_404(FinancialContribution, pk=pk)
    budget = contribution.budget
    if budget.admin_token != admin_token:
        return HttpResponseForbidden()

    contribution.is_confirmed = True
    contribution.save()

    return HttpResponseRedirect(reverse(
        'kitty:budget/admin/detail',
        args=(budget.id, budget.admin_token,)
    ))


def financial_contribution_admin_cancel(request, pk, admin_token):
    contribution = get_object_or_404(FinancialContribution, pk=pk)
    budget = contribution.budget
    if budget.admin_token != admin_token:
        return HttpResponseForbidden()

    contribution.delete()

    return HttpResponseRedirect(reverse(
        'kitty:budget/admin/detail',
        args=(budget.id, budget.admin_token,)
    ))
