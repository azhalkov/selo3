from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from apps.picture.models import Foto


class VidListView(ListView):
    template_name = 'picture/picture_detail.html'
    model = Foto

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

