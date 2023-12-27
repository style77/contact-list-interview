from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from contactlist.views import HomeView, ContactListView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view()),
    path("list/<int:pk>", ContactListView.as_view(), name="contact_list")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
