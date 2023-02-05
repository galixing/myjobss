from django.db import models

class Area(models.Model):
    pid = models.IntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    merger_name = models.CharField(max_length=255, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    pinyin = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=100, blank=True, null=True)
    first = models.CharField(max_length=50, blank=True, null=True)
    lng = models.CharField(max_length=100, blank=True, null=True)
    lat = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'area'