from Valkyrie.form.tool.form_blog_post_add import BlogPostAddForm
from Valkyrie.form.auth.form_auth_user_add import AuthUserAddForm
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def tools(request):
    tools_view = ToolsView()
    response = render(request, 'page/tool/tools.html', Context({'sections': tools_view.get_elements()}))
    return HttpResponse(response)


class ToolsView:
    sections = []

    def __init__(self):
        blog_post_add_button = [
                'fragment/modal/form/form-modal.html',                          # Modal template
                'fragment/modal/form/add-form/blog-post-add-edit-form.html',    # Form template
                BlogPostAddForm(),                                              # Form instance
                '',                                                             # ID parameter for action
                'valkyrie-page-single-listable__blog-post-add-modal',           # Modal ID
                'Make a Blog Post',                                             # Modal title text
                'btn btn-primary',                                              # Button style
                'blog-post-add',                                                # Form action
                'Make a Blog Post',                                             # Submit button text
                '',                                                             # Listable button style
                'valkyrie-fragment-form__section-form',                         # Form CSS class
                'multipart/form-data',                                          # Form enctype
            ]

        auth_user_add_button = [
                'fragment/modal/form/form-modal.html',                      # Modal template
                'fragment/modal/form/add-form/auth-user-add-form.html',     # Form template
                AuthUserAddForm(),                                          # Form instance
                '',                                                         # ID parameter for action
                'valkyrie-page-single-listable__auth-user-add-modal',       # Modal ID
                'Add an Auth User',                                         # Modal title text
                'btn btn-primary',                                          # Button style
                'auth-user-add',                                            # Form action
                'Add an Auth User',                                         # Submit button text
                '',                                                         # Listable button style
                'valkyrie-fragment-form__section-form',                     # Form CSS class
                '',                                                         # Form enctype
        ]

        blog = ['Blog',
                [
                    blog_post_add_button,
                ],
                ]

        auth = ['Authentication',
                [
                    auth_user_add_button,
                ],
                ]

        self.sections = [blog, auth, ]

    def get_elements(self):
        return self.sections
