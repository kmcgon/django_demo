from rest_framework import serializers

from .models import Requests


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Requests
        fields = ("id", "rtype", "time", "comment")


class CommentSerializer(serializers.Serializer):
    comment = serializers.CharField(required=True)
