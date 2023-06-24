from django.contrib.auth.models import User
from django.db import models


class SearchQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None ,blank=True, null=True)
    village_name = models.CharField(max_length=100, blank=True)
    city_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    pin_code = models.CharField(max_length=10, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    search_date = models.DateTimeField(auto_now_add=True)
    apiMetaValues = models.JSONField(blank=True, null=True)
    weatherTableByDate = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.city_name
