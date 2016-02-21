from _include.Chimera.Chimera.models import BlogPost, Album, Blob
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def blog_post_delete(request, blog_post_id):
    blog_post = BlogPost.objects.filter(pk=blog_post_id)
    if blog_post.count() > 0:
        blog_post = blog_post[0]
    else:
        return HttpResponseRedirect('/posts')

    album = Album.objects.filter(pk=blog_post.album_id)
    if album.count() > 0:
        album = album[0]
    else:
        return HttpResponseRedirect('/posts')

    blob_list = Blob.objects.filter(album_id=album.id)

    for blob in blob_list:
        # TODO: Delete blobs
        pass

    try:
        blog_post.delete()
        album.delete()
    except StandardError:
        return HttpResponseRedirect(reverse('blog-post', args=[blog_post.id, ]))

    return HttpResponseRedirect('/posts')
