from django.shortcuts import render
from django.views.generic import View

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import MyUserCreationForm


class IndexView(View):
    """ Главная страница """
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class SignUpView(CreateView):
    form_class = MyUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
