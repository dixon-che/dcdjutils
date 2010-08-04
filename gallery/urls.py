from django.conf.urls.defaults import *
from dcdjutils.gallery.models import Gallery, GalleryDescription, GalleryPhoto, GalleryPhotoDescription

info_dict = {
    'queryset': Gallery.objects.all(),
    'date_field': 'pub_date',
    'allow_future': 'True',
}

info_dict1 = info_dict.copy()
info_dict1['month_format']='%m'

    
urlpatterns = patterns(
    '',
    url(r'(?P<slug>[-\w]+)/$', 'dcdjutils.gallery.views.view', name='gallery-view'),
    url(r'^$', 'django.views.generic.date_based.archive_index',  info_dict, name='gallery'),
)
