from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .models import *
from .utils import *
import datetime
import json
from django.contrib.auth import authenticate, login, logout

from store.utils import cartData, cookieCartData


# Create your views here.
def createUser(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST.copy())

        if form.is_valid():
            user, created = User.objects.get_or_create(username=form.cleaned_data['email'],
                                                       email=form.cleaned_data['email'],
                                                       first_name=form.cleaned_data['first_name'],
                                                       last_name=form.cleaned_data['last_name'])

            if created:
                user.set_password(form.cleaned_data['password2'])
                user.save()
                messages.success(request, 'Account created successfully')
            else:
                messages.success(request, 'Account already exists')
        else:
            messages.error(request, 'ERROR SAVING FORM: Make sure to use a UNIQUE username '
                                    'and that your passwords match!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def loginUser(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            username = User.objects.get(email=email.lower()).username
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, 'Welcome Back!')
            else:
                print('sad!')
                messages.error(request, 'Authentication Error: Email or password is invalid')
        except:
            messages.error(request, 'Authentication Error: Email or password is invalid')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def logoutUser(request):
    logout(request)
    messages.success(request, 'You have been logged out')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def editUser(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone = request.POST.get('phone')
            customer = request.user.customer
            customer.user.first_name = first_name
            customer.user.last_name = last_name
            customer.user.email = email
            customer.phone = phone
            customer.name = first_name + ' ' + last_name
            customer.email = email
            customer.save()
            customer.user.save()
            messages.success(request, 'Account information changed')

        except:
            messages.error(request, 'Unable to change information')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def addCoupon(request):
    if request.method == 'POST':
        form = CouponForm(request.POST or None)
        if form.is_valid():
            code = form.cleaned_data.get('code')

            if request.user.is_authenticated:
                data = cartData(request)
                order = data['order']
                try:
                    coupon = Coupon.objects.get(code=code)
                    order.coupon = coupon
                    order.save()
                    messages.success(request, 'Coupon Code Successfully Applied')
                except ObjectDoesNotExist:
                    messages.info(request, 'Invalid Coupon Code')
            else:
                try:
                    coupon = Coupon.objects.get(code=code)
                    request.session['code'] = code
                    messages.success(request, 'Coupon Code Successfully Applied')
                except ObjectDoesNotExist:
                    messages.info(request, 'Invalid Coupon Code')
            return redirect('shop:checkout')
    # TODO: raise error
    return None


def updateDelivery(request):
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    order.delivery = data['delivery']

    if order.delivery == 'Shipping':
        if data['shipping']['country'] == 'Canada':
            order.shipping_cost = 15
        elif data['shipping']['country'] == 'USA':
            order.shipping_cost = 30
        else:
            order.shipping_cost = 50

    if data['is_layaway']:
        order.layaway = True
    order.save()

    order_data = {
        'delivery': order.delivery,
        'shipping_cost': order.shipping_cost,
        'is_layaway': order.layaway,
        'get_cart_total': order.get_cart_total,
    }

    return JsonResponse(order_data)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if 'code' in request.session:
        del request.session['code']

    # order delivery options are set in updateDelivery function

    if order.delivery == 'Shipping':
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            address2=data['shipping']['address2'],
            city=data['shipping']['city'],
            province=data['shipping']['province'],
            country=data['shipping']['country'],
            postal_code=data['shipping']['postal_code'],
        )
    return JsonResponse('Payment submitted...', safe=False)


def account(request):
    context = {
    }
    return render(request, 'store/account.html')



