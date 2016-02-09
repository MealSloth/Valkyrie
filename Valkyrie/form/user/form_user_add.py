from django.forms import *
from _include.Chimera.Chimera.enums import *
from _include.Chimera.Chimera.models import User
from datetime import datetime


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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).count():
            raise forms.ValidationError(u'This email address is already in use.')
        return email

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

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            gender=gender,
            join_date=join_date
        )

        user.save()
