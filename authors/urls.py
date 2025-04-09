from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='authors-detail'),

]

