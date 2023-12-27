from django.contrib import admin
from contactlist.models import Contact, ContactList

# Register your models here.

admin.site.register(ContactList)
admin.site.register(Contact)
