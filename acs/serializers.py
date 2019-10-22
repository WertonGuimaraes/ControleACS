from rest_framework import serializers

from acs.models import Acs


class AcsSerializer(serializers.HyperlinkedModelSerializer):
    pessoas = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Acs
        fields = ['id', 'name', 'modified_date', 'pessoas']