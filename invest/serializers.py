from .models import user
from rest_framework import serializers

class userserialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=user
        fields=['name','password']