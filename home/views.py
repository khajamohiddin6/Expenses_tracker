from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from .models import Profile, Expense
from decimal import Decimal

@login_required
def home(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    expenses = Expense.objects.filter(user=request.user)

    if request.method == 'POST':
        if 'update_totals' in request.POST:
            try:
                income = Decimal(request.POST.get('income', profile.income))
                expenses_total = Decimal(request.POST.get('expenses', profile.expenses))

                profile.income = income
                profile.expenses = expenses_total
                profile.balance = income - expenses_total
                profile.save()
                return redirect('/')  # Redirect after updating totals
            except ValueError as e:
                return render(request, 'home/home.html', {'profile': profile, 'expenses': expenses, 'error': f'Invalid input: {e}'})

        # Handle adding a new transaction
        text = request.POST.get('text')
        try:
            amount = Decimal(request.POST.get('amount'))  # Convert amount to Decimal
            expense_type = request.POST.get('expense_type')

            # Create new expense
            expense = Expense(name=text, amount=amount, expense_type=expense_type, user=request.user)
            expense.save()

            # Update balance based on the expense type
            if expense_type == 'Positive':  # Income
                profile.income += amount
                profile.balance += amount
            else:  # Expense
                profile.expenses += amount
                profile.balance -= amount
            profile.save()

            return redirect('/')  # Redirect after adding transaction
        except ValueError as e:
            return render(request, 'home/home.html', {'profile': profile, 'expenses': expenses, 'error': f'Invalid input: {e}'})
        
    return render(request, 'home/home.html', {'profile': profile, 'expenses': expenses})

@login_required
def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id, user=request.user)
    
    # Before deletion, update balance and profile
    if expense.expense_type == 'Positive':  # If it's an income, reduce it
        request.user.profile.income -= expense.amount
        request.user.profile.balance -= expense.amount
    else:  # If it's an expense, reduce it
        request.user.profile.expenses -= expense.amount
        request.user.profile.balance += expense.amount

    # Delete the expense from the database
    expense.delete()
    
    # Save updated profile
    request.user.profile.save()
    
    return redirect('/')  # Redirect after deleting the expense
