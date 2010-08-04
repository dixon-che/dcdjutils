from django.db import models
from django.conf import settings 
from django.dispatch import dispatcher
from django.db.models import signals
from DjHDGutils.flow import view_to_url
from django.utils.translation import ugettext_lazy as _
from DjHDGutils.templatetags.thumbnail import thumbnail
from django.utils import translation


class Gallery(models.Model): 
    pub_date = models.DateTimeField(_('Publishing date'), )
    slug_title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), )
    ico = models.ImageField(upload_to="gallery_images/ico/", null=True)
    
    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        if translation.get_language()=='ru':
            return view_to_url('gallery-view-ru', self.slug)
        else:
            return view_to_url('gallery-view-en', self.slug)
    
    def _get_title(self):
        gallerydescription = self.gallerydescription_set.filter(language=translation.get_language())
        if gallerydescription:
            return gallerydescription[0].title
        return ''
    title = property(_get_title)
    
    def _get_description(self):
        gallerydescription = self.gallerydescription_set.filter(language=translation.get_language())
        if gallerydescription:
            return gallerydescription[0].description
        return ''
    description = property(_get_description)

    def ico_thumbnail(self):
        return "<a href='%s'><img src='%s' /></a>" % (self.ico.url, 
                                                      thumbnail(self.ico.name, args = "width=100,height=100"))
    ico_thumbnail.short_description = 'Thumbnail'
    ico_thumbnail.allow_tags = True

    class Meta:
        db_table = 'gallery'
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')

class GalleryDescription(models.Model):
    gallery = models.ForeignKey(Gallery)
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'), )
    language = models.CharField(_('Language'), max_length=2,choices=settings.LANGUAGES)

    class Meta:
        unique_together = (("gallery", "language"),)

class GalleryPhoto(models.Model):
    gallery = models.ForeignKey(Gallery)
    photo = models.ImageField(upload_to="gallery_images/")
    pub_date = models.DateTimeField(_('Publishing date'), )
		
    def _get_title(self):
        galleryphotodescription = self.galleryphotodescription_set.filter(language=translation.get_language())
        if galleryphotodescription:
            return galleryphotodescription[0].title
        return ''
    title = property(_get_title)
    
    def _get_description(self):
        galleryphotodescription = self.galleryphotodescription_set.filter(language=translation.get_language())[0]
        if galleryphotodescription:
            return galleryphotodescription[0].description
        return ''
    description = property(_get_description)
    
    def photo_thumbnail(self):
        return "<a href='%s'><img src='%s' /></a>" % (self.photo.url, 
                                                      thumbnail(self.photo.name, args = "width=100,height=100"))
    photo_thumbnail.short_description = 'Thumbnail'
    photo_thumbnail.allow_tags = True

    #FIX ME: not use static string /admin/gallery/galleryphoto/
    def edit_admin_url(self):
        return "/admin/gallery/galleryphoto/%d/" % self.id
    
class GalleryPhotoDescription(models.Model):
    gallery_photo = models.ForeignKey(GalleryPhoto)
    title = models.CharField(_('Title'), max_length=255)
    description = models.TextField(_('Description'), )
    language = models.CharField(_('Language'), max_length=2,choices=settings.LANGUAGES)

    class Meta:
        unique_together = (("gallery_photo", "language"),)
        