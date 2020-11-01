import order
from django.conf.global_settings import SESSION_EXPIRE_AT_BROWSER_CLOSE
from django.shortcuts import render

import cart
from .tasks import order_created
# Create your views here.
# очистка корзины
if SESSION_EXPIRE_AT_BROWSER_CLOSE:

    cart.clear()
# запуск асинхронной задачи
order_created.delay(order.id)