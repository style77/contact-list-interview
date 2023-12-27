from typing import Any
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView
from contactlist.forms import UploadContactForm
from contactlist.models import ContactList, Contact


class HomeView(FormView):
    template_name = "home.html"
    form_class = UploadContactForm
    success_url = reverse_lazy("contact_list")

    def form_valid(self, form):
        contact_list = form.handle_file(self.request)
        self.success_url = reverse_lazy("contact_list", kwargs={"pk": contact_list.pk})
        return super().form_valid(form)


class ContactListView(DetailView):
    model = ContactList
    template_name = "contact_list.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.filter(contact_list=context["object"])
        return context
