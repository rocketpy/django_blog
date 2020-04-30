from rest_framework import serializers
from .model import Language


class LanguageSerializer(serializers.Modelserializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'paradigm')
