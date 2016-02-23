from django.http import HttpResponseRedirect, HttpResponse
from Valkyrie.form.order.form_order_add import OrderAddForm
from django.core.urlresolvers import reverse


def order_add(request, post_id):
    if request.method == 'POST':
        form = OrderAddForm(request.POST)
        if form.is_valid():
            order_id = form.process(post_id)
            return HttpResponseRedirect(reverse('order', args=[order_id, ]))
        else:
            return HttpResponse("Invalid form")
    else:
        return HttpResponseRedirect('/orders')
