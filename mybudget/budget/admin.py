from django.contrib import admin
from .models import Category, Income, Expense


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Adjust this based on the fields you want to display


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date', 'category')
    list_filter = ('date', 'category')
    search_fields = ('amount', 'category__name')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date', 'category')
    list_filter = ('date', 'category')
    search_fields = ('amount', 'category__name')
