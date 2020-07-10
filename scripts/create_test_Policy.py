from rest_api.models import *
CHINA = Country.objects.get(code='CHN')
JPN = Country.objects.get(code="JPN")
obj,created = BorderPolicy.objects.update_or_create(
    country=JPN,
    defaults = {
    "quarantine" : BorderPolicy.MANDATORY_CENTRALIZED,
    "status": BorderPolicy.FALSE,
    "url" : 'https://www.mofa.go.jp/ca/fna/page4e_001053.html#section2',
    "exemptions" : {'Nationals'}
    }
)
