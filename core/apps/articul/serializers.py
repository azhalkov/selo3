from rest_framework import serializers
# from models import Articul
from apps.articul.models import Articul


class ArticulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articul
        # fields = '__all__'
        exclude = ['id', 'artikuls', 'status', 'data_vidan', 'slug', 'is_oplata', 'nomer']