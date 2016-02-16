from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import Billing
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def billing(request, billing_id):
    billing_view = BillingView(billing_id=billing_id)
    response = render(request, 'page/abstract/single-listable.html', Context(billing_view.get_elements()))
    return HttpResponse(response)


class BillingView(SingleListableView):
    def __init__(self, billing_id):
        current_billing = Billing.objects.filter(pk=billing_id)
        if not current_billing.values().count() > 0:
            return
        else:
            current_billing = current_billing[0]

        id = [current_billing.id, ]

        kwargs = {
            'id': id,
        }

        SingleListableView.__init__(self, **kwargs)
