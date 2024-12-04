
from django.urls import path
from .views import home, delete_expense

urlpatterns = [
    path('', home, name='home'),
    path('delete_expense/<int:expense_id>/', delete_expense, name='delete_expense'),
]
