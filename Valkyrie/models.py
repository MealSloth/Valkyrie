from django.db import models


# Gender
MALE = 0
FEMALE = 1
OTHER = 2

Gender = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
)


# PostStatus
ACTIVE = 0
SATURATED = 1
INACTIVE = 2

PostStatus = (
    (ACTIVE, 'Active'),
    (SATURATED, 'Saturated'),
    (INACTIVE, 'Inactive'),
)


class User(models.Model):
    id = models.CharField(primary_key=True, editable=False)
    consumer_id = models.CharField(editable=False)
    chef_id = models.CharField(editable=False)
    location_id = models.CharField(editable=False)
    billing_id = models.CharField(editable=False)
    profile_photo_id = models.CharField(editable=False)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    gender = models.IntegerField(choices=Gender)
