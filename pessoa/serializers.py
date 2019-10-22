from rest_framework import serializers

from pessoa.models import Pessoa


class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'acs', 'name', 'modified_date']