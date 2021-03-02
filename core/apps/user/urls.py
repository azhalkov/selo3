from django.urls import path
from django.urls import path
from django.contrib.auth import views
from .views import SignUpView, IndexView
# from .views import *


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
]
