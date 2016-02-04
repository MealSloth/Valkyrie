from django.forms import *
from Siren.models import Contact


class ContactForm(Form):
    first_name = CharField(max_length=30, required=True)
    last_name = CharField(max_length=30, required=True)
    email = EmailField(max_length=254, required=True)
    message = CharField(max_length=1000, required=False)

    def process(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']

        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message,
        )

        contact.save()

        return Contact.objects.filter(email=email).values()[0].get('id')
