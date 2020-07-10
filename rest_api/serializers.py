from rest_framework import serializers
from rest_api.models import *
from rest_api.utils import *

class ChoiceField(serializers.ChoiceField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._reverse_choices = reverse_dict(self._choices)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        try:
            return self._reverse_choices[str(data)]
        except KeyError:
            self.fail('invalid_choice', input=data)

class SetField(serializers.Field):
    def to_representation(self, obj):
        return list(obj)


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


class FlightStatusSerializer(serializers.ModelSerializer):
    from_country = CountrySerializer(read_only=True)
    to_country = CountrySerializer(read_only=True)

    class Meta:
        model = FlightStatus
        fields = [
            'id',
            'from_country',
            'to_country',
            'status',
            'time',
        ]

class BorderPolicySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    quarantine = ChoiceField(choices=BorderPolicy.QUARANTINE_CHOICES)
    status = ChoiceField(choices=BorderPolicy.STATUS_CHOICES)
    exemptions =SetField(read_only=True)

    class Meta:
        model = BorderPolicy
        fields = [
            'id',
            'country',
            'quarantine',
            'status',
            'url',
            'exemptions',
            'time'
        ]


class FlightStatusProdSerializer(FlightStatusSerializer):
    exemptions = SetField(source='to_country.exemptions')

    class Meta:
        model = FlightStatus
        fields = [
            'id',
            'from_country',
            'to_country',
            'status',
            'time',
            'exemptions'
        ]


class BorderPolicyProdSerializer(BorderPolicySerializer):
    forbidden_arrival = serializers.SlugRelatedField(read_only=True,slug_field='code',many=True,source='country.forbidden_arrival')
    forbidden_departure = serializers.SlugRelatedField(read_only=True,slug_field='code',many=True,source='country.forbidden_departure')
    class Meta:
        model = BorderPolicy
        fields = [
            'id',
            'forbidden_arrival',
            'forbidden_departure',
            'country',
            'quarantine',
            'status',
            'url',
            'exemptions',
            'time'
        ]
