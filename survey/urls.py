from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_near_miss, name='create_near_miss'),
    path('', views.list_near_miss, name='list_near_miss'),
    path('<int:pk>/', views.detail_near_miss, name='detail_near_miss'),
    path('<int:pk>/edit/', views.edit_near_miss, name='edit_near_miss'),
    path('<int:pk>/delete/', views.delete_near_miss, name='delete_near_miss'),
    path('export/', views.export_csv, name='export_csv'),
]
