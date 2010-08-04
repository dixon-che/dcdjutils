from django.utils.translation import ugettext_lazy as _
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import Http404

from dcdjutils.gallery.models import Gallery, GalleryDescription, GalleryPhoto, GalleryPhotoDescription


def view(request, slug):
    gallery = get_object_or_404(Gallery, slug=slug)
    return render_to_response('gallery/gallery_view.html', RequestContext(request,dict(gallery=gallery, 
                                                                                        title=_('Portfolio'))))
