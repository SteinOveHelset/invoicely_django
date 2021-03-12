from django.contrib.auth.models import User
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    org_number = models.CharField(max_length=255, blank=True, null=True)
    first_invoice_number = models.IntegerField(default=1)
    bankaccount = models.CharField(max_length=266, blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='teams', on_delete=models.CASCADE)
    email = models.EmailField(blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    zipcode = models.CharField(max_length=255, blank=True, null=True)
    place = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return '%s' % self.name