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
    user_login_id = models.CharField(editable=False)
    consumer_id = models.CharField(editable=False)
    chef_id = models.CharField(editable=False)
    location_id = models.CharField(editable=False)
    billing_id = models.CharField(editable=False)
    profile_photo_id = models.CharField(editable=False)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    gender = models.IntegerField(choices=Gender)

    @staticmethod
    def get_model_name():
        return User.__class__.__name__

    @staticmethod
    def get_field_names():
        return User._meta.get_all_field_names()

    class Meta:
        db_table = "User"


def get_user_list(model):
    return model.objects
