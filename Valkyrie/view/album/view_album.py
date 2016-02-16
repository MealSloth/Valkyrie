from Valkyrie.view.abstract.view_single_listable import SingleListableView
from _include.Chimera.Chimera.models import Album
from django.http import HttpResponse
from django.template import Context
from django.shortcuts import render


def album(request, album_id):
    album_view = AlbumView(album_id=album_id)
    response = render(request, 'page/abstract/single-listable.html', Context(album_view.get_elements()))
    return HttpResponse(response)


class AlbumView(SingleListableView):
    def __init__(self, album_id):
        current_album = Album.objects.filter(pk=album_id)
        if not current_album.values().count() > 0:
            return
        else:
            current_album = current_album[0]

        id = [('Album', current_album.id), ]

        kwargs = {
            'id': id,
        }

        SingleListableView.__init__(self, **kwargs)
