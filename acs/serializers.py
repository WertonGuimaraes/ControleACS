from rest_framework import serializers

from models import Acs


class AcsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Acs
        fields = ['id', 'name', 'modified_date']