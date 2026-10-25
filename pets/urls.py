from django.urls import path
from . import views

urlpatterns = [
    path('', views.PetListView.as_view(), name='pet_list'),
    path('add/', views.PetCreateView.as_view(), name='pet_add'),
    path('<int:pk>/', views.PetDetailView.as_view(), name='pet_detail'),
    path('<int:pk>/edit/', views.PetUpdateView.as_view(), name='pet_edit'),
    path('<int:pk>/delete/', views.PetDeleteView.as_view(), name='pet_delete'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    path('tags/add/', views.TagCreateView.as_view(), name='tag_add'),
]