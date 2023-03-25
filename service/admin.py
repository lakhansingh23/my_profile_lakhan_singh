from django.contrib import admin
from service.models import contact
class contact_admin(admin.ModelAdmin):
    pass
admin.site.register(contact,contact_admin)
# Register your models here.
