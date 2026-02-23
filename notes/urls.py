from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.list_notes),
    path('notes/<int:pk>/', views.delete_note),
]