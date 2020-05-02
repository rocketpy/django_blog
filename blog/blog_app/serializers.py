from rest_framework import serializers
from .model import Language


class LanguageSerializer(serializers.Modelserializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'paradigm')

        
# this will return url        
"""
class LanguageSerializer(serializers.HyperlinkedModelserializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')
"""
