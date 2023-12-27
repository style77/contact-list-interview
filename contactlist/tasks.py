from contactlist.models import Contact, ContactList
from celery import shared_task
from django.core.exceptions import ValidationError

import pandas as pd


def insert_contacts(df, contact_list):
    return Contact.objects.bulk_create(
        [
            Contact(
                contact_list=contact_list,
                name=row["name"],
                phone=row["phone"],
                email=row["email"],
            )
            for _, row in df.iterrows()
        ]
    )


# Code of this parse_x functions could be just in case statement
# However we could update these in future
def parse_xlsx_contactlist(path):
    return pd.read_excel(path, engine="openpyxl")


def parse_csv_contactlist(path):
    return pd.read_csv(path)


@shared_task()
def handle_contact_list_task(contact_list_id: int):
    contact_list = ContactList.objects.get(id=contact_list_id)

    with contact_list.import_file as file:
        path = file.path
        ext = file.path.split(".")[-1]

        match ext:
            case "xls" | "xlsx":
                df = parse_xlsx_contactlist(path)
            case "csv":
                df = parse_csv_contactlist(path)
            case _:
                raise ValidationError("Wrong extension")

        insert_contacts(df, contact_list)
        contact_list.processed = True
        contact_list.save()
