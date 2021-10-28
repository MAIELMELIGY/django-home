from django.contrib import admin

from .models import Header,About,mision_vision,why_home , Client ,SubCategory ,Tag, Header ,About , Contact , Service ,Projects_in,SubCategory ,ProductHdl,ProductTuya


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'subject')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
admin.site.register(Header)
admin.site.register(About)
admin.site.register(Client)
admin.site.register(mision_vision)
admin.site.register(why_home)
admin.site.register(Service)
admin.site.register(Projects_in)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(ProductHdl)
admin.site.register(ProductTuya)


