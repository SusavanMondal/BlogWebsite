from django.contrib import admin
from .models import contact_list
from .models import contactform
# Register your models here.

admin.site.register(contact_list)
admin.site.register(contactform)