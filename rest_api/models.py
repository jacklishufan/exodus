from django.db import models
from django_mysql.models import SetTextField
# Create your models here.


class Country(models.Model):
    code = models.CharField(max_length=3,unique=True,blank=False,null=False,primary_key=True)
    name = models.TextField(null=False,blank=False)
    name_cn = models.TextField(null=False, blank=False)

    @property
    def latest_policy(self):
        if self.policies.filter().exists():
            return self.policies.filter().order_by('-time').first()
        else:
            return None

    @property
    def exemptions(self):
        policy = self.latest_policy
        if policy:
            return policy.exemptions
        else:
            return set()

    @property
    def forbidden_arrival(self):
        qs = FlightStatus.objects.filter(to_country=self,status=FlightStatus.FALSE).prefetch_related('from_country')
        return [x.from_country for x in qs]

    @property
    def forbidden_departure(self):
        qs = FlightStatus.objects.filter(from_country=self, status=FlightStatus.FALSE).prefetch_related('to_country')
        return [x.to_country for x in qs]

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
    status = models.CharField(choices=STATUS_CHOICES,max_length=1,default=UNKNOWN)
    time = models.DateTimeField(auto_now=True)

class BorderPolicy(models.Model):
    MANDATORY_CENTRALIZED = 'M'
    MANDATORY_SELF = 'D'
    FREE_SELF = 'S'
    NO_POLICY = 'N'
    UNKNOWN = 'U'
    TRUE = "T"
    FALSE = "F"
    QUARANTINE_CHOICES = [
        (MANDATORY_CENTRALIZED, 'Mandatory and centrailzed '),
        (MANDATORY_SELF, 'Mandatory self quarantine'),
        (FREE_SELF,'Self quarantine advice with no enforcement mechanism'),
        (NO_POLICY, 'No policy whatsoever'),
        (UNKNOWN, 'Unknown'),
    ]
    STATUS_CHOICES = [
        (TRUE, 'true'),
        (FALSE, 'false'),
        (UNKNOWN,'unknown')
    ]
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=False, blank=False,related_name="policies")
    quarantine = models.CharField(choices=QUARANTINE_CHOICES,max_length=1,default=UNKNOWN)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1,default=UNKNOWN)
    url = models.TextField(null=True,blank=True)
    exemptions = SetTextField(base_field=models.CharField(max_length=20))
    time = models.DateTimeField(auto_now=True)
