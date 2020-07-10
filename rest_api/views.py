from django.shortcuts import render

# Create your views here.
from django.db.models import Q
from django.http import JsonResponse
from django.db.models import Sum, Max
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
from rest_framework.pagination import PageNumberPagination
from .serializers import *
from datetime import datetime,timedelta


class CountryListView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = CountrySerializer
    def get_queryset(self):
        qs = Country.objects.filter()
        request = self.request
        name_cn = request.GET.get('name_cn')
        if name_cn:
            qs = qs.filter(name_cn=name_cn)
            # if not qs.exists():
            #     return Response({"messege":"400 Bad Request"},status=400)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class VisaStatusListView(mixins.CreateModelMixin, generics.ListAPIView):
    serializer_class = VisaStatusSerializer
    def get_queryset(self):
        return VisaStatus.objects.filter(out_dt=None)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CountryDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    serializer_class = CountrySerializer
    # lookup_field = 'ticker'
    queryset = Country.objects.all()

class VisaStatusDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    serializer_class = VisaStatusSerializer
    # lookup_field = 'ticker'
    queryset = VisaStatus.objects.filter(out_dt=None)

class FlightStatusListAPIView(generics.ListAPIView):
    serializer_class = FlightStatusSerializer

    def get_queryset(self):
        request = self.request
        qs = FlightStatus.objects.filter()
        from_region = request.GET.get('from_region')
        to_region = request.GET.get('to_region')
        if from_region:
            qs = qs.filter(from_country=from_region)
        if to_region:
            qs = qs.filter(to_country=to_region)
        return qs

class BorderPolicyListAPIView(generics.ListAPIView):
    serializer_class = BorderPolicySerializer

    def get_queryset(self):
        request = self.request
        qs = BorderPolicy.objects.filter()
        region = request.GET.get('region')
        if region:
            qs = qs.filter(country=region)
        return qs


class FlightStatusProdAPIView(FlightStatusListAPIView):
    serializer_class = FlightStatusProdSerializer

class BorderPolicyProdAPIView(BorderPolicyListAPIView):
    serializer_class = BorderPolicyProdSerializer
