# apps/picture/urls
from django.template import Template
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from .views import *
from . import views
from django.views.generic.list import ListView

from apps.picture.models import Foto

# from apps.picture.views import

urlpatterns = [
    path('', TemplateView.as_view(template_name='picture/picture.html'), name='picture'),
    path('vid/', VidListView.as_view(), name='vid'),
    # path('adres/', AdresView.as_view(template_name='dom/forms/adres_form.html'), name='adres'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)