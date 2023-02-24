from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView
from .models import Basket, Order

@login_required
def orders(request):
    orders = request.user.orders.order_by('-timestamp')
    return render(request, 'orders/orders.html', {'orders': orders})

@login_required
def cancel(request):
    if request.method == 'POST':
        message = Order.cancel(request.POST['id'])
        messages.info(request, message)
        return redirect('products:home')

def new(request):
    basket = request.user.basket
    if request.method == 'GET' or request.POST['total'] != basket.total:
        return render(request, 'orders/new.html', {'basket': basket})
    order = Order.create(
        user = request.user,
        items = basket.items,
        total = basket.total,
        status = 'PENDING'
    )
    return redirect('orders:complete', kwargs={'id': order.id})

def complete(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == 'GET':
        return render(request, 'orders/complete.html', {'order': order})
    success = mock_payment_api(request.POST)
    if success:
        messages.info(request, 'Order successful')
        order.status = 'COMPLETED'
        order.save()
        return redirect('products:home')
    else:
        messages.info(request, 'Payment error')
        return render(request, 'orders/complete.html', {'order': order})

class BasketView(DetailView):
    model = Basket
    template_name = 'orders/basket.html'

    def get_object(self, *args):
        return self.request.user.basket

def mock_payment_api(data):
    print(data)
    return True