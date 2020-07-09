from django.urls import path
from rest_api import views

urlpatterns = [
    path('countries/', views.CountryListView.as_view()),
    path('countries/<str:pk>/', views.CountryDetailAPIView.as_view()),
    path('visastatus/', views.VisaStatusListView.as_view()),
    path('visastatus/<int:pk>/', views.VisaStatusDetailAPIView.as_view()),
]
