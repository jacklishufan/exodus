from rest_api.models import *

data = {
    "country": "MEX",
    "can_entry": 'T',
}
country = Country.objects.get(code=data['country'])
print(country.name)
data['country'] = country
VisaStatus.objects.create(**data)
