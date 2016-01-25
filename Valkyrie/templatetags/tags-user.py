from django import template


register = template.Library()


def generate_entry(item_list):
    response = "<tr>"
    for item in item_list:
        response += "<td><h5>" + item + "</h5></td>"
    return response + "</tr>"


def generate_link(item, page_name):
    return "<a href=\"/" + page_name + "/" + item + "\">" + item + "</a>"


@register.simple_tag
def entry_for_key(dictionary, key):
    return dictionary.get(key)


@register.simple_tag
def user_entry(user_list):
    response = ""
    for dictionary in user_list:
        response += generate_entry([
            generate_link(dictionary.get("id"), "user"),
            dictionary.get("first_name") + " " + dictionary.get("last_name"),
            dictionary.get("email"),
            dictionary.get("phone_number"),
            dictionary.get("date_of_birth"),
        ])
    return response


@register.simple_tag
def post_entry(post_list):
    response = ""
    for dictionary in post_list:
        response += generate_entry([
            dictionary.get("id"),
            # More stuff
        ])
