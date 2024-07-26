# budget/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import IncomeForm, ExpenseForm, CategoryForm
from .models import Income, Expense, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import datetime


@login_required
def create_category_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('index')  # Redirect to the index page or another relevant page
    else:
        form = CategoryForm()
    return render(request, 'budget/create_category.html', {'form': form})


@login_required
def delete_category_view(request, pk):
    category = get_object_or_404(Category, pk=pk, user=request.user)
    if request.method == 'POST':
        category.delete()
        return redirect('index')
    return render(request, 'budget/delete_category.html', {'category': category})


@login_required
def index_view(request):
    user = request.user
    categories = Category.objects.filter(user=user)

    return render(request, 'budget/index.html', {
        'categories': categories
    })


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'budget/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('monthly_report')
    else:
        form = AuthenticationForm()
    return render(request, 'budget/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    return render(request, 'budget/logout.html')


@login_required
def add_income_view(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            return redirect('monthly_report')
    else:
        form = IncomeForm()
    categories = Category.objects.all()
    return render(request, 'budget/add_income.html', {'form': form, 'categories': categories})


@login_required
def add_expense_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect('monthly_report')
    else:
        form = ExpenseForm()
    categories = Category.objects.all()
    return render(request, 'budget/add_expense.html', {'form': form, 'categories': categories})


@login_required
def monthly_report_view(request):
    user = request.user
    categories = Category.objects.filter(user=user)
    today = datetime.date.today()
    first_day = today.replace(day=1)
    incomes = Income.objects.filter(user=request.user, date__gte=first_day).values('category__name').annotate(total=Sum('amount'))
    expenses = Expense.objects.filter(user=request.user, date__gte=first_day).values('category__name').annotate(total=Sum('amount'))
    return render(request, 'budget/monthly_report.html', {'categories': categories, 'incomes': incomes, 'expenses': expenses})



