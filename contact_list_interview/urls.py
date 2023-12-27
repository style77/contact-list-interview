from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from contactlist.views import HomeView, SuccessView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", HomeView.as_view()),
    path("success/", SuccessView.as_view(), name="success_page")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
