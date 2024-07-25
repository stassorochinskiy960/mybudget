from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_income/', views.add_income_view, name='add_income'),
    path('add_expense/', views.add_expense_view, name='add_expense'),
    path('monthly_report/', views.monthly_report_view, name='monthly_report'),
]
