from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
    """ Главная страница """
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')