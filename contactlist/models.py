from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class ContactList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(...)
    import_file = models.FileField(...)
    processed = models.BooleanField(default=False)


class Contact(models.Model):
    contact_list = models.ForeignKey(ContactList, on_delete=models.CASCADE)
    name = models.CharField()
    phone = models.CharField()
    email = models.EmailField()
