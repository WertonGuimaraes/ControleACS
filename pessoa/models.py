# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from acs.models import Acs


class Pessoa(models.Model):
    acs = models.ForeignKey(Acs, related_name='pessoas', on_delete=models.CASCADE)
    name = models.CharField(max_length=254, null=False, blank=False)
    modified_date = models.DateTimeField(auto_now=True, null=True)
