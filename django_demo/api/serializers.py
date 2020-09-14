from rest_framework import serializers

from .models import Requests


class RequestSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for the Requests table."""
    class Meta:
        model = Requests
        fields = ("id", "rtype", "time", "comment")
