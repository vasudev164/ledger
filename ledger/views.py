from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Account, Transaction
from .forms import AccountForm, TransactionForm, AddTransactionForm
from django.urls import reverse
from datetime import date


# Create your views here.
def add(obj):
    ctotal = 0
    dtotal = 0
    for o in obj:
        ctotal += o.cash_in
        dtotal += o.cash_out
    return ctotal, dtotal, ctotal-dtotal


accounts = Account.objects.all()
all_transactions = Transaction.objects.all()
all_ctotal, all_dtotal, all_total = add(all_transactions)


def index(request):
    accounts = Account.objects.all()
    all_transactions = Transaction.objects.all()
    all_ctotal, all_dtotal, all_total = add(all_transactions)
    today_transactions = []
    for transaction in all_transactions:
        if transaction.transaction_added == date.today():
            today_transactions.append(transaction)
    today_ctotal, today_dtotal, today_total = add(today_transactions)
    context = {
        "accounts": accounts,
        "transactions": all_transactions,
        'today_transactions': today_transactions,
        'all_ctotal': all_ctotal,
        'all_dtotal': all_dtotal,
        'all_total': all_total,
        'today_ctotal': today_ctotal,
        'today_dtotal': today_dtotal,
        'today_total': today_total
    }
    return render(request, 'ledger/index.html', context)


def transactions(request, account_id):
    account = Account.objects.get(id=account_id)
    today_transactions = []
    all_transactions = Transaction.objects.all()
    acc_transactions = []
    for transaction in all_transactions:
        if transaction.account.name == account.name:
            acc_transactions.append(transaction)
        if transaction.transaction_added == date.today():
            today_transactions.append(transaction)
    context = {
        'acc_transactions': acc_transactions,
        'account': account,
        'today_transactions': today_transactions
    }
    return render(request, 'ledger/transactions.html', context)


def new_account(request):
    form = AccountForm()
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ledger:index'))
    context = {'form': form}
    return render(request, 'ledger/new_account.html', context)


def new_transaction(request, account_id):
    account = Account.objects.get(id=account_id)
    form = TransactionForm()
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            new_account = form.save(commit=False)
            new_account.account = account
            new_account.save()
            return HttpResponseRedirect(reverse('ledger:index'))
    context = {'form': form,
               'account': account}
    return render(request, 'ledger/new_transaction.html', context)


def add_transaction(request):
    form = AddTransactionForm()
    if request.method == 'POST':
        form = AddTransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ledger:index'))
    context = {'form': form,
               'accounts': Account.objects.all()}
    return render(request, 'ledger/add_transaction.html', context)


def ledger_summary(request):
    totals = []
    for account in accounts:
        acc_transactions = []
        try:
            acc_transactions = Transaction.objects.filter(account=account)
        except Transaction.DoesNotExist:
            pass
        s = list((add(acc_transactions)))
        s.append(account)
        totals.append(tuple(s))
    context = {'totals': totals,
               'all_ctotal': all_ctotal,
               'all_dtotal': all_dtotal,
               'all_total': all_total}
    return render(request, 'ledger/ledger_summary.html', context)
for account in accounts:
    print(account)