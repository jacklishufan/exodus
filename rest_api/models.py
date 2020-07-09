from django.db import models

# Create your models here.

class Country(models.Model):
    code = models.CharField(max_length=3,unique=True,blank=False,null=False,primary_key=True)
    name = models.TextField(null=False,blank=False)
    name_cn = models.TextField(null=False, blank=False)

class VisaStatus(models.Model):
    TRUE = "T"
    FALSE = "F"
    UNKNOWN = "U"

    STATUS_CHOICES = [
        (TRUE, 'true'),
        (FALSE, 'false'),
        (UNKNOWN,'unknown')
    ]

    country = models.ForeignKey(Country,on_delete=models.CASCADE,null=False,blank=False)
    # can_apply = models.BooleanField()
    can_entry = models.CharField(choices=STATUS_CHOICES,max_length=1)
    detail = models.TextField(null=True,blank=True)
    in_dt = models.DateTimeField(auto_now=True)
    out_dt = models.DateTimeField(null=True)
    source_url = models.TextField(null=True)

class VirusStats(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False, blank=False)
    in_dt = models.DateTimeField(auto_now=True)
    out_dt = models.DateTimeField(null=True)
    curr_infection = models.BigIntegerField(null=True)
    total_cured =  models.BigIntegerField(null=True)
    total_death =  models.BigIntegerField(null=True)
    total_infection = models.BigIntegerField(null=True)

class FlightStatus(models.Model):

    TRUE = "T"
    FALSE = "F"
    UNKNOWN = "U"

    STATUS_CHOICES = [
        (TRUE, 'true'),
        (FALSE, 'false'),
        (UNKNOWN,'unknown')
    ]
    from_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False, blank=False,related_name="departure")
    to_country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False, blank=False,related_name="arrival")
    status = models.CharField(choices=STATUS_CHOICES,max_length=1)
    in_dt = models.DateTimeField(auto_now=True)
    out_dt = models.DateTimeField(null=True)

