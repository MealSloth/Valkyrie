from _include.Chimera.Chimera.models import Order, Post, Consumer, User
from _include.Chimera.Chimera.enums import OrderType
from datetime import datetime
from django.forms import *


def consumers():
    response = []
    for user in User.objects.all().values():
        if Consumer.objects.filter(pk=user.get('consumer_id')).count() > 0:
            response.append((user.get('consumer_id'), user.get('first_name') + ' ' + user.get('last_name')))
    return tuple(response)


class OrderAddForm(Form):
    consumer_id = ChoiceField(choices=consumers(), required=True)
    order_type = ChoiceField(choices=OrderType.OrderType)
    amount = IntegerField()

    def process(self, post_id):
        post = Post.objects.filter(pk=post_id)
        if post.count() > 0:
            post = post[0]
        else:
            return

        consumer = Consumer.objects.filter(pk=self.cleaned_data['consumer_id'])
        if consumer.count() > 0:
            consumer = consumer[0]
        else:
            return

        user = User.objects.filter(consumer_id=consumer.id)
        if user.count() > 0:
            user = user[0]
        else:
            return

        post_id = post.id
        consumer_id = consumer.id
        chef_id = post.chef_id
        location_id = consumer.location_id
        billing_id = user.billing_id
        order_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")
        amount = self.cleaned_data['amount']

        if amount > post.capacity:
            return

        order = Order(
            post_id=post_id,
            consumer_id=consumer_id,
            chef_id=chef_id,
            location_id=location_id,
            billing_id=billing_id,
            order_time=order_time,
            amount=amount,
        )

        try:
            order.save()
        except StandardError:
            return

        return order.id
