from django.urls import path

from .views import GalleryView

from .views import GalleryView, CreatePostView # new form level

urlpatterns = [
    path("", GalleryView.as_view(), name="gellery"),
    path("image/", CreatePostView.as_view(), name="add_image")
]