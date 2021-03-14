# apps/articul/urls
# from django.template import Template
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
# from . import views
from .views import *
from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='articul/home.html'), name='articul'),
    path('newart/', ArticulView.as_view(template_name='articul/articul_form.html'), name='newart'),
    path('artlist/', views.ArtikulListView.as_view(), name='artlist'),
    path('ar/',views.artikulList, name='ar'),
    #      name='new_categori'),
    # path('add_document/', DomDokumentView.as_view(template_name='dom/forms/document_form.html'),
    #      name='new_document'),
    # path('add_foto_dom/', FotoDomView.as_view(), name='addfotodom'),
    # path('adres/', AdresView.as_view(template_name='dom/forms/adres_form.html'), name='adres'),
    # path('artikul/', ArtikulView.as_view(template_name='dom/forms/articul_form.html'), name='artikul'),
    # path('person/', PersonView.as_view(template_name='dom/forms/person_form.html'), name='new_person'),
    #
    # path('adresa/', views.AdresListView.as_view(), name='adresa'),
    # path('adresa/<slug:slug>/', AdresDetailView.as_view(), name='adresa_detail'),
    # path('search/', SearchAdresaView.as_view(), name='search'),
    #
    # path('prodavcu/', TemplateView.as_view(template_name='dom/info/prodavcu.html'), name='prodavcu'),
    # path('partner/', TemplateView.as_view(template_name='dom/info/partner.html'), name='partner'),
    # path('ceni/', TemplateView.as_view(template_name='dom/info/ponjatnie_ceni.html'), name='ceni'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
