from rest_api.models import *

with open('scripts/country.csv') as f:
    countries = [x.split() for x in f.readlines()]
countries = [{
    "code":x[0],
    "name":" ".join(x[4:-1]),
    "name_cn":x[-1]
    } for x in countries]

for country in countries:
        print(country)
        Country.objects.update_or_create(defaults=country,code = country['code'])
        # print("INFO: Creating Country {}".format(country['name']))
