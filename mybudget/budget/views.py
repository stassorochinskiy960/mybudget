# budget/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import IncomeForm, ExpenseForm
from .models import Income, Expense, Category
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import datetime



def index_view(request):
    return render(request, 'budget/index.html')


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
    today = datetime.date.today()
    first_day = today.replace(day=1)
    incomes = Income.objects.filter(user=request.user, date__gte=first_day).values('category__name').annotate(total=Sum('amount'))
    expenses = Expense.objects.filter(user=request.user, date__gte=first_day).values('category__name').annotate(total=Sum('amount'))
    return render(request, 'budget/monthly_report.html', {'incomes': incomes, 'expenses': expenses})


