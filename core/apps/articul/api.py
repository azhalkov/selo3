# from articul.models import Articul
# https://www.youtube.com/watch?v=TmDetBtk5rw
from rest_framework import viewsets, permissions

from .models import Articul
from  .serializers import ArticulSerializer


class ArticulViewSet(viewsets.ModelViewSet):
    queryset = Articul.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ArticulSerializer


