from django.urls import path
from . import views


app_name = 'ledger'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:account_id>', views.transactions, name='transactions'),
    path('new_account', views.new_account, name='new_account'),
    path('new_transaction/<int:account_id>', views.new_transaction, name='new_transaction'),
    path('add_transaction', views.add_transaction, name='add_transaction'),
    path('ledger_summary', views.ledger_summary, name='ledger_summary'),
]
