from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from django.views.generic import ListView, CreateView  # new
from django.urls import reverse_lazy  # new

from .forms import UpdateForm  # new

from .models import Update


class CertifictesView(ListView):
    model = Update
    template_name = "certificates.html"

class CreateUpdateView(CreateView):  # new
    model = Update
    form_class = UpdateForm
    template_name = "images.html"
    success_url = reverse_lazy("certificates")