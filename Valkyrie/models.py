from django.db.models import *
from enums import *


class User(Model):
    id = CharField(primary_key=True, editable=False)
    user_login_id = CharField(editable=False)
    consumer_id = CharField(editable=False)
    chef_id = CharField(editable=False)
    location_id = CharField(editable=False)
    billing_id = CharField(editable=False)
    profile_photo_id = CharField(editable=False)
    email = EmailField(max_length=254)
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)
    phone_number = CharField(max_length=30)
    date_of_birth = CharField(max_length=30)
    gender = IntegerField(choices=Gender.Gender)

    class Meta:
        db_table = "users"


class Post(Model):
    id = CharField(primary_key=True, editable=False)
    chef_id = CharField(editable=False)
    location_id = CharField(editable=False)
    album_id = CharField(editable=False)
    name = CharField(max_length=50)
    description = CharField(max_length=255)
    order_count = IntegerField()
    capacity = IntegerField()
    status = IntegerField(choices=PostStatus.PostStatus)
    expire_time = CharField(max_length=30)

    class Meta:
        db_table = "posts"


class Order(Model):
    id = CharField(primary_key=True, editable=False)
    post_id = CharField(editable=False)
    consumer_id = CharField(editable=False)
    chef_id = CharField(editable=False)
    location_id = CharField(editable=False)
    billing_id = CharField(editable=False)
    order_summary_id = CharField(editable=False)
    order_status = IntegerField(choices=OrderStatus.OrderStatus)
    order_type = IntegerField(choices=OrderType.OrderType)
    amount = IntegerField()

    class Meta:
        db_table = "orders"


class Location(Model):
    id = CharField(primary_key=True, editable=False)
    user_id = CharField(editable=False)
    purpose = IntegerField(choices=LocationPurpose.LocationPurpose)
    type = IntegerField(choices=LocationType.LocationType)
    address_line_one = CharField()
    address_line_two = CharField()
    city = CharField()
    state = CharField()
    country = CharField()
    zip = CharField()

    class Meta:
        db_table = "locations"


class Consumer(Model):
    id = CharField(primary_key=True, editable=False)
    user_id = CharField(editable=False)
    location_id = CharField(editable=False)

    class Meta:
        db_table = "consumers"


class Album(Model):
    id = CharField(primary_key=True, editable=False)
    post_id = CharField(editable=False)

    class Meta:
        db_table = "albums"


class OrderTime(Model):
    id = CharField(editable=False)
    order_id = CharField(editable=False)
    status = IntegerField(choices=OrderStatus.OrderStatus)
    time = CharField(editable=False)

    class Meta:
        db_table = "order_times"


class FavoritePost(Model):
    id = CharField(editable=False)
    consumer_id = CharField(editable=False)
    post_id = CharField(editable=False)

    class Meta:
        db_table = "favorite_posts"


class FavoriteChef(Model):
    id = CharField(editable=False)
    consumer_id = CharField(editable=False)
    chef_id = CharField(editable=False)

    class Meta:
        db_table = "favorite_chefs"
