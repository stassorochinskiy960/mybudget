from django.urls import path
from .views import index_view, add_note_view, delete_note_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_note_view, name='add_note'),
    path('delete/<int:pk>/', delete_note_view, name='delete_note'),
]
