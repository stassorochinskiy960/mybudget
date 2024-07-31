# budget/forms.py

from django import forms
from .models import Income, Expense, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount', 'date', 'category']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'date', 'category']

