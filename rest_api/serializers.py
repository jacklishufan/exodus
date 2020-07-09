from rest_framework import serializers
from rest_api.models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            'code',
            'name',
            'name_cn',
            # 'in_dt',
            # 'out_dt'
        ]

class VisaStatusSerializer(serializers.ModelSerializer):
    country_name_cn = serializers.CharField(
            source='country.name_cn', read_only=True)
    class Meta:
        model = VisaStatus
        fields = [
            'id',
            'country',
            'can_entry',
            'detail',
            'source_url',
            'in_dt',
            'country_name_cn'
            # 'in_dt',
            # 'out_dt'
        ]

