from django.urls import path

from .views import CertifictesView

from .views import CertifictesView, CreateUpdateView # new

urlpatterns = [
    path("", CertifictesView.as_view(), name="add_image"),
    path("images/", CreateUpdateView.as_view(), name="add_images")  # new
]