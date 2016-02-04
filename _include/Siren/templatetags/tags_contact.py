from django import template
from Siren.models import ContactEmail, Contact


register = template.Library()


@register.simple_tag
def email_from_email_id(contact_email_id):
    if ContactEmail.objects.filter(id=contact_email_id).exists():
        return ContactEmail.objects.filter(id=contact_email_id).values()[0].get('email')
    else:
        return 'This email address has not been recorded!'


@register.simple_tag
def email_from_contact_id(contact_id):
    if Contact.objects.filter(id=contact_id).exists():
        return Contact.objects.filter(id=contact_id).values()[0].get('email')
    else:
        return 'This email address has not been recorded!'


@register.simple_tag
def name_from_contact_id(contact_id):
    if Contact.objects.filter(id=contact_id).exists():
        return Contact.objects.filter(id=contact_id).values()[0].get('first_name')
    else:
        return 'This email address has not been recorded!'
