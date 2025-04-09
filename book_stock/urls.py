from django.urls import path
from . import views

urlpatterns = [
    path('availability/', views.BookAvailabilityListCreateView.as_view(), name='availability_list_create'),
    path('availability/<int:pk>/', views.BookAvailabilityDetailView.as_view(), name='availability-detail'),
]
