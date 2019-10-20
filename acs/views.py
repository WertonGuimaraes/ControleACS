from rest_framework import viewsets
from serializers import AcsSerializer
from models import Acs


class AcsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Acs.objects.all().order_by('id')
    serializer_class = AcsSerializer