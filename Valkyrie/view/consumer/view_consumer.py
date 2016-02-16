from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import Consumer
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def consumer(request, consumer_id):
    consumer_view = ConsumerView(consumer_id=consumer_id)
    response = render(request, 'page/abstract/single-listable.html', Context(consumer_view.get_elements()))
    return HttpResponse(response)


class ConsumerView(SingleListableView):
    def __init__(self, consumer_id):
        current_consumer = Consumer.objects.filter(pk=consumer_id)
        if not current_consumer.values().count() > 0:
            return
        else:
            current_consumer = current_consumer[0]

        id = [current_consumer.id, ]

        kwargs = {
            'id': id,
        }

        SingleListableView.__init__(self, **kwargs)
