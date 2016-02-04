from django.forms import *
from Siren.models import ContactEmail


class ContactEmailForm(Form):
    email = EmailField(max_length=254, required=True)

    def process(self):
        email = self.cleaned_data['email']

        contact_email = ContactEmail(email=email)

        contact_email.save()

        return ContactEmail.objects.filter(email=email).values()[0].get('id')
