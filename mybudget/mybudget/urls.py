# mybudget/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('budget.urls')),
    path('notebook', include('notebook.urls')),
]
