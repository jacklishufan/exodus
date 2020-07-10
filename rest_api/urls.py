from django.urls import include, path
from rest_api import views


dev_patterns = [
    path('flight-status/', views.FlightStatusListAPIView.as_view()),
    path('border-policy/', views.BorderPolicyListAPIView.as_view()),
]


prod_patterns = [
    path('flight-status/', views.FlightStatusProdAPIView.as_view()),
    path('border-policy/', views.BorderPolicyProdAPIView.as_view()),
]


urlpatterns = [
    path('countries/', views.CountryListView.as_view()),
    path('countries/<str:pk>/', views.CountryDetailAPIView.as_view()),
    path('visastatus/', views.VisaStatusListView.as_view()),
    path('visastatus/<int:pk>/', views.VisaStatusDetailAPIView.as_view()),
    path('dev/', include(dev_patterns)),
    path('prod/', include(prod_patterns)),
]
