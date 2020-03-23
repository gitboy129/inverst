from .models import user
from rest_framework import serializers

class userserialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=user
        fields=['name','password']

class lofSerialize(serializers.Serializer):
    code = serializers.CharField(max_length=6)
    shortname = serializers.CharField(max_length=16)
    longname = serializers.CharField(max_length=80)
    lx = serializers.CharField(max_length=10)
    pyname = serializers.CharField(max_length=80)
