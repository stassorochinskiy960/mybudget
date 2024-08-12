from django.urls import path
from . import views
from .views import custom_login_redirect_view

urlpatterns = [
    path('', views.index_view, name='index'),
    path('print_report/', views.print_report_view, name='print_report'),
    path('create_category/', views.create_category_view, name='create_category'),
    path('monthly_report/', views.monthly_report_view, name='monthly_report'),
    path('login_redirect/', custom_login_redirect_view, name='login_redirect'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add_income/', views.add_income_view, name='add_income'),
    path('add_expense/', views.add_expense_view, name='add_expense'),
    path('monthly_report/', views.monthly_report_view, name='monthly_report'),
]
