from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context
from django.shortcuts import render
from django.core.urlresolvers import reverse
from form.contact.form_contact_email import ContactEmailForm
from form.contact.form_contact import ContactForm


def home(request):
    if request.method == 'POST':
        form = ContactEmailForm(request.POST)
        if form.is_valid():
            contact_email_id = form.process()
            url = reverse('thanks', args=['email', contact_email_id])
            return HttpResponseRedirect(url)
    else:
        response = render(request, 'page/home.html', Context({'form': ContactEmailForm}))
        return HttpResponse(response)


def about(request):
    if request.method == 'POST':
        form = ContactEmailForm(request.POST)
        if form.is_valid():
            contact_email_id = form.process()
            url = reverse('thanks', args=['email', contact_email_id])
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect('/')
    else:
        response = render(request, 'page/about.html', Context({'form': ContactEmailForm()}))
        return HttpResponse(response)


def blog(request):
    response = render(request, 'page/blog.html')
    return HttpResponse(response)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_id = form.process()
            url = reverse('thanks', args=['contact', contact_id])
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect('/')
    else:
        response = render(request, 'page/contact.html', Context({'form': ContactForm()}))
        return HttpResponse(response)


def thanks(request, thank_type, unique_id):
    response = render(request, 'page/thanks.html', Context({'id': unique_id, 'type': thank_type}))
    return HttpResponse(response)


def consumer(request):
    response = render(request, 'page/consumer.html')
    return HttpResponse(response)


def producer(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_id = form.process()
            url = reverse('thanks', args=['contact', contact_id])
            return HttpResponseRedirect(url)
        else:
            return HttpResponseRedirect('/')
    else:
        response = render(request, 'page/producer.html', Context({'form': ContactForm()}))
        return HttpResponse(response)

