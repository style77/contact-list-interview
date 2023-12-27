from django.db import models
from contactlist.validators import validate_file_extension


class ContactList(models.Model):
    name = models.CharField()
    import_file = models.FileField(upload_to="contact_lists/", validators=[validate_file_extension])
    processed = models.BooleanField(default=False)


class Contact(models.Model):
    contact_list = models.ForeignKey(ContactList, on_delete=models.CASCADE)
    name = models.CharField()
    phone = models.CharField()
    email = models.EmailField()
