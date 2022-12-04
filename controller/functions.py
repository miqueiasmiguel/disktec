import datetime


def update_payment_status(clients):
    for client in clients:
        days_until_pay = client.expiration_date - datetime.date.today()

        if days_until_pay.days < 7 and days_until_pay.days > 0:
            client.payment_status = 1  # próximo
            client.save()
        elif days_until_pay.days < 0:
            client.payment_status = 2  # atrasado
            client.save()
        elif client.last_payment.month < datetime.date.today().month:
            client.payment_status = 3  # aguardando pagamento
            client.save()


def machine_count(Model):
    query = Model.objects.order_by().values("installments_value").distinct()
    machines = []
    for row in query:
        machines.append(row["installments_value"])

    machines_count = {}
    for machine in machines:
        machines_count[machine] = Model.objects.filter(installments_value=machine).count()
    return machines_count
