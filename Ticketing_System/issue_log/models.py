from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Client(models.Model):
    client_name = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.client_name


class Severity(models.Model):
    severity_index = models.CharField(max_length=10)

    def __unicode__(self):
        return self.severity_index


class Issue(models.Model):
    issue_description = models.TextField(max_length=200, blank=False, verbose_name="Description")
    client_name = models.ForeignKey(Client, blank=False, verbose_name="Client")
    severity_index = models.ForeignKey(Severity, blank=False, verbose_name="Severity")
    issued_by = models.ForeignKey(User, related_name="%(class)s_requests_created", verbose_name="Issued By")
    is_priority = models.NullBooleanField(blank=True, null=True, verbose_name="Priority")
    is_open = models.BooleanField(default=True, verbose_name="Resolved")
    issued_on = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Issued On")
