from django.contrib import admin
#from django.utils.translation import ugettext_lazy as _
from dcdjutils.gallery.models import Gallery, GalleryDescription, GalleryPhoto, GalleryPhotoDescription


class GalleryPhotoInline(admin.TabularInline):
    model = GalleryPhoto
    extra = 3
    template = 'gallery/edit_inline/tabular.html'


class GalleryDescriptionInline(admin.TabularInline):
    model = GalleryDescription
    max_num = 2
    extra = 1
    fk_name = 'gallery'
    fields = ('language', 'title', 'description')


class GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('slug_title', )}
    list_display = ('id', 'slug', 'pub_date', 'ico_thumbnail')
    list_filter = ('pub_date', )

    class Media:
        js = ('tiny_mce/js/tiny_mce.js',
              'MochiKit/js/MochiKit.js',
              'tiny_mce/js/textarea.js',
              )

    inlines = [GalleryDescriptionInline,
               GalleryPhotoInline]

admin.site.register(Gallery, GalleryAdmin)


class GalleryPhotoDescriptionInline(admin.TabularInline):
    model = GalleryPhotoDescription
    max_num = 2
    extra = 1
    fields = ('language', 'title', 'description')


class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'gallery', 'pub_date', 'photo_thumbnail')
    list_filter = ('gallery', 'pub_date')

    inlines = [GalleryPhotoDescriptionInline]

admin.site.register(GalleryPhoto, GalleryPhotoAdmin)
