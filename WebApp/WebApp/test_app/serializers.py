from rest_framework import serializers
from .models import TestClass

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestClass
        fields = ['id', 'counter']