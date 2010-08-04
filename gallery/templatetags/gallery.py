from django import template
from dcdjutils.gallery.models import Gallery
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils import translation

register = template.Library()

@register.simple_tag
def gallery_list():
    galleries = Gallery.objects.all().order_by('-pub_date')
    LANGUAGE_CODE = translation.get_language()
    return render_to_string('gallery/tag_gallery_list.html', dict(galleries=galleries, LANGUAGE_CODE=LANGUAGE_CODE))
