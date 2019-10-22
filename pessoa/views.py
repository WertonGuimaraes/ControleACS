# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets

from pessoa.models import Pessoa
from pessoa.serializers import PessoaSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pessoa.objects.all().order_by('id')
    serializer_class = PessoaSerializer
