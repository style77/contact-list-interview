from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from contactlist.forms import UploadContactForm


class HomeView(FormView):
    template_name = "home.html"
    form_class = UploadContactForm
    success_url = reverse_lazy('success_page')

    def form_valid(self, form):
        form.handle_file(self.request)
        return super().form_valid(form)


class SuccessView(TemplateView):
    template_name = "success.html"
