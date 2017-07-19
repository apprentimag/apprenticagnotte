from django.conf.urls import url
from django.views.decorators.http import require_GET, require_POST

from . import views

app_name = 'kitty'
urlpatterns = [
    url(r'^$',
        require_GET(views.BudgetListView.as_view()),
        name='budget/list'),
    url(r'^create/$',
        require_POST(views.budget_create),
        name='budget/create'),
    url(r'^(?P<pk>[a-zA-Z0-9]+)/$',
        require_GET(views.BudgetDetailView.as_view()),
        name='budget/detail'),
    url(r'^(?P<pk>[a-zA-Z0-9]+)/admin/(?P<admin_token>[a-zA-Z0-9]+)/$',
        require_GET(views.BudgetAdminDetailView.as_view()),
        name='budget/admin/detail'),
    url(r'^(?P<pk>[a-zA-Z0-9]+)/admin/(?P<admin_token>[a-zA-Z0-9]+)/update/$',
        require_POST(views.budget_admin_update),
        name='budget/admin/update'),
    url(r'^(?P<budget_id>[a-zA-Z0-9]+)/financial_contributions/create/$',
        require_POST(views.financial_contribution_create),
        name='financial_contribution/create'),
    url(r'^financial_contributions/(?P<pk>[0-9]+)/admin/(?P<admin_token>[a-zA-Z0-9]+)/confirm/$',
        require_POST(views.financial_contribution_admin_confirm),
        name='financial_contribution/admin/confirm'),
    url(r'^financial_contributions/(?P<pk>[0-9]+)/admin/(?P<admin_token>[a-zA-Z0-9]+)/cancel/$',
        require_POST(views.financial_contribution_admin_cancel),
        name='financial_contribution/admin/cancel'),
]
