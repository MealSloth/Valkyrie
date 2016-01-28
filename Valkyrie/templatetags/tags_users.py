from django import template
from Valkyrie.enums import *


register = template.Library()


@register.simple_tag
def entry_for_gender(dictionary):
    return Gender.Gender[int(dictionary.get("gender"))][1]


@register.simple_tag
def entry_for_dob(dictionary):
    return dictionary.get("date_of_birth")[:-16]


@register.simple_tag
def generate_link_with_key(dictionary, key, page_name):
    return "<a href=\"/" + page_name + "/" + dictionary.get(key) + "\">" + dictionary.get(key) + "</a>"


@register.simple_tag
def entry_for_key(dictionary, key):
    return dictionary.get(key)
