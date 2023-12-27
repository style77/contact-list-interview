from django import forms
from contactlist.validators import validate_file_extension
from contactlist.tasks import handle_contact_list_task
from contactlist.models import ContactList


class UploadContactForm(forms.Form):
    name = forms.CharField(label="Contact list name")
    file = forms.FileField(
        widget=forms.FileInput(),
        label="Contact list file",
        validators=[validate_file_extension],
    )

    def handle_file(self, request):
        # TODO we can iterate over all files to allow user to upload more than one file
        file = request.FILES["file"]

        contact_list = ContactList(name=self.cleaned_data["name"], import_file=file)
        contact_list.save()

        handle_contact_list_task.delay(contact_list.id)
