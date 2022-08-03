from rest_framework import serializers
from rest_framework.utils.serializer_helpers import ReturnDict

from .models import Url
import random
import string


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ('real_url','generated_url','view_count')

    @property
    def data(self):
        ret = super(UrlSerializer, self).data
        return ReturnDict(ret, serializer=self)