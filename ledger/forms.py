from django import forms
from .models import Account, Transaction


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name']
        labels = {'name': 'name'}


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['cash_in', 'cash_out', 'particular']
        labels = {'cash_in': 'credit',
                  'cash_out': 'debit',
                  'particular': 'particular'}


class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['account', 'cash_in', 'cash_out', 'particular']
        labels = {'cash_in': 'credit',
                  'cash_out': 'debit',
                  'particular': 'particular',
                  'account': 'Account Name'}
        widgets = {
            'account': forms.TextInput(attrs={'list': 'accounts', 'autocomplete': 'off'})
        }
