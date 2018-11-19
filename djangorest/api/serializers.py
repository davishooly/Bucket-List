# first lets make an import of the serializer from thr DRF
from rest_framework import serializers

from .models import BucketList


class BucketSerializer(serializers.ModelSerializer):
    """ serializer to map the model instance into JSON format """
    class Meta:
        """ to map serializer fields with model field """
        model = BucketList
        fields = ("id", "name", "date_created", "date_modified")
        read_only_fields = ("date_created", "date_modified")
