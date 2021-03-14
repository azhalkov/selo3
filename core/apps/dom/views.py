from django.shortcuts import render
from django.views import View
from apps.dom.models import Adres
from apps.dom.forms import AdresForm
# from django.views.generic.list import ListView
# from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect


class AdresView(View):
    """ Класс форма для добавления адреса объекта"""
    template_name = 'dom/forms/adres_form.html'
    form_class = AdresForm
    model = Adres

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})
