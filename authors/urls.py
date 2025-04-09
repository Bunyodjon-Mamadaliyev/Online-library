from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.AuthorListCreateView.as_view(), name='author_list_create'),

]