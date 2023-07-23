from django.shortcuts import render

# Create your views here Admin level.
from django.views.generic import ListView
from .models import Post

# Form lavel
from django.views.generic import ListView, CreateView  # new
from django.urls import reverse_lazy  # new

from .forms import PostForm # new
from .models import Post

# Admin lavel
class GalleryView(ListView):
    model = Post
    template_name = "gallery.html"

# form   lavel
class CreatePostView(CreateView):  # new
    model = Post
    form_class = PostForm
    template_name = "image.html"
    success_url = reverse_lazy("gallery")