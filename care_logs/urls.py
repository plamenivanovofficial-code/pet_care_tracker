from django.urls import path
from . import views

urlpatterns = [
    path('', views.CareActivityListView.as_view(), name='activity_list'),
    path('add/', views.CareActivityCreateView.as_view(), name='activity_add'),
    path('<int:pk>/', views.CareActivityDetailView.as_view(), name='activity_detail'),
    path('<int:pk>/edit/', views.CareActivityUpdateView.as_view(), name='activity_edit'),
    path('<int:pk>/delete/', views.CareActivityDeleteView.as_view(), name='activity_delete'),
]