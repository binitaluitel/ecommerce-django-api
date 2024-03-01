from ecommerce.models import *
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =product 
        fields = "__all__"