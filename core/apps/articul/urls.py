# apps/articul/urls
# from django.template import Template
from rest_framework import routers
from .api import ArticulViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
# from . import views
from .views import *
from . import views

router = routers.DefaultRouter()
router.register('api/articul', ArticulViewSet, 'apiarticul')

urlpatterns = [
    path('', TemplateView.as_view(template_name='articul/home.html'), name='articul'),
    path('newart/', ArticulView.as_view(template_name='articul/articul_form.html'), name='newart'),
    path('artlist/', views.ArtikulListView.as_view(), name='artlist'),
    path('artlist/<slug:slug>/', views.ArticulDetailView.as_view(template_name='articul/articul_detail.html'),
         name='articul_detail'),
    path('ar/',views.artikulList, name='ar'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls