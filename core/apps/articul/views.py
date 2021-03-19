# apps/articul/views
from django.shortcuts import render
from django.views import View
from apps.articul.models import Articul
from apps.picture.models import Foto
from apps.articul.forms import ArticulForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect


class ArticulView(View):
    """ Класс форма для добавления адреса объекта"""
    template_name = 'articul/articul_form.html'
    form_class = ArticulForm
    model = Articul

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})


class ArtikulListView(ListView):
    template_name = 'articul/articul_list.html'
    model = Articul


def artikulList(request):
    artik = Articul.objects.all()
    return render(request, 'articul/ar_list.html', {'artikul_list': artik})


class ArticulDetailView(DetailView):
    model = Articul
    template_name = 'articul/articul_detail.html'
    # queryset = Foto.objects.order_by('-art')
    # context_object_name = 'art'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['foto'] = Foto.objects.order_by('-art')



        # context['now'] = timezone.now()
        return context
