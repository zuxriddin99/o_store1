from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Zakaz berilgani dogrisinda mijoza sms boradi
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order_id)
    message = 'Dear {},\n\nYou have succesfully placed an order.\n You order id is {}.'.format(order.first_name,
                                                                                               order_id)

    mail_sent = send_mail(subject,
                          message,
                          'zux.828@gmail.com',
                          [order.email])
    return mail_sent
