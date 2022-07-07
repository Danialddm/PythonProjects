from typing import Tuple

from django.contrib import admin
from PassMngSite.myapp.models import Publisher, Author, Book
# Register and add your models here.
from django.contrib.auth.models import Permission


class AutorAdmin(admin.ModelAdmin):#class author az class django.admin.modeladmin ersbari mokonad.
    list_display = ('first_name','last_name','email') #tamme peykar bandi class modeladmin ra negah midarad va list_display ra b an ezafeh mikonad.
    search_fields = ('first_name','last_name')#add search bar for fields
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','address')
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date',)#tuple--filter ba zaman.
    date_hierarchy = 'publication_date' #filter ba sal va mah.
    ordering = ('-publication_date',)#tartib nozooli.
    fields = ('title', 'authors', 'publisher')#fieldhaye form ra neshan midahad kr emkane edit darand ya na.
    filter_horizontal = ('authors',)#baraye many to many emkane entekhab chand gozine ra faraham mikonad.
    raw_id_fields = ('publisher',)# select bar asase id
##########################################################
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Author,AutorAdmin)#farzand argomane dovom
admin.site.register(Book,BookAdmin)
admin.site.register(Permission)
###########################################################
#admin.site.site_header = "ddm_Administration"

