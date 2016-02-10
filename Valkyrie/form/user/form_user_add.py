from _include.Chimera.Chimera.models import User, UserLogin, Consumer, Chef, Location, Billing, Album, ProfilePhoto
from _include.Chimera.Chimera.enums import *
from datetime import datetime
from django.forms import *


def date(date_list):
    response = ""
    for item in date_list:
        if len(str(item)) < 2:
            response += "0" + item + "-"
        else:
            response += item + "-"
    response = response[:-1]
    response += "T00:00:00.000000"
    return response


def years():
    response = []
    now = datetime.utcnow()
    for i in range(1900, now.year + 1):
        response.append([i, str(i)])
    return tuple(response)


def days():
    response = []
    for i in range(1, 32):
        response.append([i, str(i)])
    return tuple(response)


class UserAddForm(Form):
    first_name = CharField(max_length=30, required=True)
    last_name = CharField(max_length=30, required=True)
    email = EmailField(max_length=254, required=True)
    phone_number = CharField(max_length=30, required=True)
    dob_year = ChoiceField(choices=years(), required=True)
    dob_month = ChoiceField(choices=Months.Months, required=True)
    dob_day = ChoiceField(choices=days(), required=True)
    gender = ChoiceField(choices=Gender.Gender, required=True)
    password = CharField(max_length=255, required=True, widget=PasswordInput())
    password_confirm = CharField(max_length=255, required=True, widget=PasswordInput())

    def clean_email(self):
        email = self.cleaned_data['email']
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError('This email address is already in use.')
        return email

    def clean(self):
        cleaned_data = super(UserAddForm, self).clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if not password == password_confirm:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data

    def process(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        phone_number = self.cleaned_data['phone_number']
        gender = self.cleaned_data['gender']
        date_of_birth = date([
            self.cleaned_data['dob_year'],
            self.cleaned_data['dob_month'],
            self.cleaned_data['dob_day'],
        ])
        join_date = datetime.utcnow()
        password = self.cleaned_data['password']

        temp_user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            gender=gender,
            join_date=join_date
        )

        temp_user.save()

        if not User.objects.filter(id=temp_user.id).values().count() > 0:
            return

        user = User.objects.filter(id=temp_user.id).values()[0]

        temp_user_login = UserLogin(
            id=user.get('user_login_id'),
            user_id=user.get('id'),
            username=user.get('email'),
            password=password,
        )

        temp_user_login.save()

        if not UserLogin.objects.filter(id=temp_user_login.id).values().count() > 0:
            user.delete()
            return

        user_login = UserLogin.objects.filter(id=temp_user_login.id).values()[0]

        temp_location = Location(
            id=user.get('location_id'),
            user_id=user.get('id'),
        )

        temp_location.save()

        if not Location.objects.filter(id=temp_location.id).values().count() > 0:
            user.delete()
            user_login.delete()
            return

        location = Location.objects.filter(id=temp_location.id).values()[0]

        temp_consumer = Consumer(
            id=user.get('consumer_id'),
            user_id=user.get('id'),
            location_id=location.get('id'),
        )

        temp_consumer.save()

        if not Consumer.objects.filter(id=temp_consumer.id).values().count() > 0:
            user.delete()
            user_login.delete()
            location.delete()
            return

        consumer = Consumer.objects.filter(id=temp_consumer.id).values()[0]

        temp_chef = Chef(
            id=user.get('chef_id'),
            user_id=user.get('id'),
            location_id=location.get('id'),
        )

        temp_chef.save()

        if not Chef.objects.filter(id=temp_chef.id).values().count() > 0:
            user.delete()
            user_login.delete()
            location.delete()
            consumer.delete()
            return

        chef = Chef.objects.filter(id=temp_chef.id).values()[0]

        temp_billing = Billing(
            id=user.get('billing_id'),
            user_id=user.get('id'),
            consumer_id=consumer.get('id'),
            chef_id=chef.get('id'),
            location_id=location.get('id')
        )

        temp_billing.save()

        if not Billing.objects.filter(id=temp_billing.id).values().count() > 0:
            user.delete()
            user_login.delete()
            consumer.delete()
            chef.delete()
            location.delete()
            return

        billing = Billing.objects.filter(id=temp_billing.id).values()[0]

        temp_album = Album()

        if not Album.objects.filter(id=temp_album.id).values().count() > 0:
            user.delete()
            user_login.delete()
            consumer.delete()
            chef.delete()
            location.delete()
            billing.delete()
            return

        album = Album.objects.filter(id=temp_album.id).values()[0]

        temp_profile_photo = ProfilePhoto(
            id=user.get('profile_photo_id'),
            album_id=album.get('id'),
            user_id=user.get('id'),
        )

        temp_profile_photo.save()

        if not ProfilePhoto.objects.filter(id=temp_profile_photo.id).values().count() > 0:
            user.delete()
            user_login.delete()
            consumer.delete()
            chef.delete()
            location.delete()
            billing.delete()
            album.delete()
            return

        profile_photo = ProfilePhoto.objects.filter(id=temp_profile_photo.id).values()[0]
