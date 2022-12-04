import datetime
from dateutil.relativedelta import relativedelta
from django.shortcuts import redirect, render
from insurance.forms import InsuranceForm
from rent.forms import RentForm
from sale.forms import SaleForm
from service.forms import ServiceForm
from notes.forms import NoteForm
from insurance.models import InsuranceClient
from rent.models import RentClient
from sale.models import SaleClient
from service.models import ServiceClient
from notes.models import Note
from daily_income.models import DailyIncome
from controller.functions import update_payment_status, machine_count


def home(request):
    return render(request, "home.html")


def insurance(request):
    show_form = True
    show_search = True
    show_total = True

    clients = InsuranceClient.objects.all().order_by('expiration_date')
    total = sum(clients.values_list("installments_value", flat=True))
    machines_count = machine_count(InsuranceClient)
    update_payment_status(clients)

    query = request.GET.get("search_bar")
    if query != "" and query is not None:
        q1 = clients.filter(name__icontains=query)
        q2 = clients.filter(cpf__icontains=query)
        q3 = clients.filter(rg__icontains=query)
        clients = q1.union(q2, q3).order_by('expiration_date')

        show_form = False

    if request.method == "POST":
        form = InsuranceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(insurance)
    else:
        form = InsuranceForm()

    context = {
        "form": form,
        "clients": clients,
        "machines_count": machines_count,
        "total": total,
        "show_form": show_form,
        "show_search": show_search,
        "show_total": show_total,
    }
    return render(request, "insurance.html", context)


def rent(request):
    show_form = True
    show_search = True
    show_total = True

    clients = RentClient.objects.all().order_by('expiration_date')
    total = sum(clients.values_list("installments_value", flat=True))
    machines_count = machine_count(RentClient)
    update_payment_status(clients)

    query = request.GET.get("search_bar")
    if query != "" and query is not None:
        q1 = clients.filter(name__icontains=query)
        q2 = clients.filter(cpf__icontains=query)
        q3 = clients.filter(rg__icontains=query)
        clients = q1.union(q2, q3).order_by('expiration_date')

        show_form = False

    if request.method == "POST":
        form = RentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(rent)
    else:
        form = RentForm()

    context = {
        "form": form,
        "clients": clients,
        "machines_count": machines_count,
        "total": total,
        "show_form": show_form,
        "show_search": show_search,
        "show_total": show_total,
    }
    return render(request, "rent.html", context)


def sale(request):
    show_form = True
    show_search = True

    clients = SaleClient.objects.all().order_by('name')
    query = request.GET.get("search_bar")
    if query != "" and query is not None:
        q1 = clients.filter(name__icontains=query)
        q2 = clients.filter(cpf__icontains=query)
        q3 = clients.filter(rg__icontains=query)
        clients = q1.union(q2, q3).order_by('name')

        show_form = False

    if request.method == "POST":
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(sale)
    else:
        form = SaleForm()

    context = {
        "form": form,
        "clients": clients,
        "show_form": show_form,
        "show_search": show_search,
    }
    return render(request, "sale.html", context)


def service(request):
    show_form = True
    show_search = True

    clients = ServiceClient.objects.all().order_by('name')
    query = request.GET.get("search_bar")
    if query != "" and query is not None:
        q1 = clients.filter(name__icontains=query)
        q2 = clients.filter(cpf__icontains=query)
        q3 = clients.filter(rg__icontains=query)
        clients = q1.union(q2, q3).order_by('name')

        show_form = False

    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(service)
    else:
        form = ServiceForm()

    context = {
        "form": form,
        "clients": clients,
        "show_form": show_form,
        "show_search": show_search,
    }
    return render(request, "service.html", context)


def notes(request):
    notes_query = Note.objects.all().order_by("date")
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(notes)
    else:
        form = NoteForm()
    context = {"notes": notes_query, "form": form}
    return render(request, "notes.html", context)


def daily_income(request):
    date = request.GET.get("search_date")
    type = request.GET.get("search_type")
    if type == "all":
        query = DailyIncome.objects.all().filter(date=date)
    elif type == "insurance_rent":
        query = DailyIncome.objects.all().filter(date=date, type='insurance') | DailyIncome.objects.all().filter(date=date, type='rent')
    elif type == "sale_service":
        query = DailyIncome.objects.all().filter(date=date, type='sale') | DailyIncome.objects.all().filter(date=date, type='service')
    else:
        query = DailyIncome.objects.all().filter(date=date, type=type)

    total = sum(query.values_list("value", flat=True))
    context = {"query": query, "total":total}
    return render(request, "daily_income.html", context)


def monthly_income(request):
    month = request.GET.get("search_month")
    year = request.GET.get("search_year")
    type = request.GET.get("search_type")
    months = range(1,13)
    years = [2022, 2023]

    query = None

    if month !=0 and year !=0:
        if type == "all":
            query = DailyIncome.objects.all().filter(date__month=month, date__year=year)
        elif type == "sale_service":
            query = DailyIncome.objects.all().filter(date__month=month, date__year=year, type='sale') | DailyIncome.objects.all().filter(date__month=month, date__year=year, type='service')
        elif type == "insurance_rent":
            query = DailyIncome.objects.all().filter(date__month=month, date__year=year, type='insurance') | DailyIncome.objects.all().filter(date__month=month, date__year=year, type='rent')
        else:
            query = DailyIncome.objects.all().filter(date__month=month, date__year=year, type=type)
    
    if query:
        total = sum(query.values_list("value", flat=True))
    else:
        total = 0
    context = {'months':months, 'years':years, 'query': query, 'total':total}
    return render(request, "monthly_income.html", context)


def pay(request, contract, pk):
    if contract == "insurance":
        client = InsuranceClient.objects.get(pk=pk)
        client.last_payment = datetime.date.today()
        client.expiration_date += relativedelta(months=1)
        client.payment_status = 4  # pago
        client.save()

        try:
            query = DailyIncome.objects.get(name=client.name, value=client.installments_value, type=contract)
        except DailyIncome.DoesNotExist:
            query = None
        if not query:
            income = DailyIncome()
            income.name = client.name
            income.value = client.installments_value
            income.type = contract
            income.save()

        return redirect(insurance)

    elif contract == "rent":
        client = RentClient.objects.get(pk=pk)
        client.last_payment = datetime.date.today()
        client.expiration_date += relativedelta(months=1)
        client.payment_status = 4  # pago
        client.save()

        try:
            query = DailyIncome.objects.get(name=client.name, value=client.installments_value, type=contract)
        except DailyIncome.DoesNotExist:
            query = None
        if not query:
            income = DailyIncome()
            income.name = client.name
            income.value = client.installments_value
            income.type = contract
            income.save()

        return redirect(rent)
    
    elif contract == "sale":
        client = SaleClient.objects.get(pk=pk)
        client.payment_status = 4  # pago
        client.save()

        income = DailyIncome()
        income.name = client.name
        income.value = client.total
        income.type = contract
        income.save()

        return redirect(sale)
    
    elif contract == "service":
        client = ServiceClient.objects.get(pk=pk)
        client.payment_status = 4  # pago
        client.save()

        income = DailyIncome()
        income.name = client.name
        income.value = client.total
        income.type = contract
        income.save()

        return redirect(service)


def edit(request, contract, pk):
    show_form = True
    show_search = False
    show_total = False
    clients = {}

    if contract == "insurance":
        client = InsuranceClient.objects.get(id=pk)
        if request.method == "POST":
            form = InsuranceForm(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                return redirect(insurance)
        else:
            form = InsuranceForm(instance=client)
        context = {
            "form": form,
            "clients": clients,
            "show_form": show_form,
            "show_search": show_search,
            "show_total": show_total,
        }
        return render(request, "insurance.html", context)

    elif contract == "rent":
        client = RentClient.objects.get(id=pk)
        if request.method == "POST":
            form = RentForm(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                return redirect(rent)
        else:
            form = RentForm(instance=client)
        context = {
            "form": form,
            "clients": clients,
            "show_form": show_form,
            "show_search": show_search,
            "show_total": show_total,
        }
        return render(request, "rent.html", context)

    elif contract == "sale":
        client = SaleClient.objects.get(id=pk)
        if request.method == "POST":
            form = SaleForm(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                return redirect(sale)
        else:
            form = SaleForm(instance=client)
        context = {
            "form": form,
            "clients": clients,
            "show_form": show_form,
            "show_search": show_search,
        }
        return render(request, "sale.html", context)

    elif contract == "service":
        client = ServiceClient.objects.get(id=pk)
        if request.method == "POST":
            form = ServiceForm(request.POST, request.FILES, instance=client)
            if form.is_valid():
                form.save()
                return redirect(service)
        else:
            form = ServiceForm(instance=client)
        context = {
            "form": form,
            "clients": clients,
            "show_form": show_form,
            "show_search": show_search,
        }
        return render(request, "service.html", context)


def delete(request, contract, pk):
    if contract == "insurance":
        client = InsuranceClient.objects.get(id=pk)
        client.delete()
        return redirect(insurance)

    elif contract == "rent":
        client = RentClient.objects.get(id=pk)
        client.delete()
        return redirect(rent)

    elif contract == "sale":
        client = SaleClient.objects.get(id=pk)
        client.delete()
        return redirect(sale)

    elif contract == "service":
        client = ServiceClient.objects.get(id=pk)
        client.delete()
        return redirect(service)


def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return redirect(notes)


def print_contract(request, contract, pk):
    if contract == "insurance":
        client = InsuranceClient.objects.get(pk=pk)
        context = {"client": client}
        return render(request, "insurance_contract.html", context)
    elif contract == "rent":
        client = RentClient.objects.get(pk=pk)
        context = {"client": client}
        return render(request, "rent_contract.html", context)


def print_client_list(request, contract, value):
    print(f"Valor {value}")
    if contract == "insurance":
        clients = InsuranceClient.objects.all().filter(installments_value = float(value))
    elif contract == "rent":
        clients = RentClient.objects.all().filter(installments_value = float(value))
    context = {"clients":clients}
    return render(request, "client_list.html", context)