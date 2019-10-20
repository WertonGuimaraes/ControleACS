# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Acs(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    modified_date = models.DateTimeField(auto_now=True, null=True)
