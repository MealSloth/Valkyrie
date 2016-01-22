from django import template


register = template.Library()


@register.filter
def get_entry_for_key(dictionary, key):
    return dictionary.get(key)


@register.simple_tag
def user_entry(user_list):
    response = ""
    for dictionary in user_list:
        response += "<tr>"
        response += "<td><h5>" + dictionary.get("id") + "</h5></td>"
        response += "<td><h5>" + dictionary.get("first_name") + " " + dictionary.get("last_name") + "</h5></td>"
        response += "<td><h5>" + dictionary.get("email") + "</h5></td>"
        response += "<td><h5>" + dictionary.get("phone_number") + "</h5></td>"
        response += "<td><h5>" + dictionary.get("date_of_birth") + "</h5></td>"
        response += "</tr>"
    return response
