from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, password_validation
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import *
from .models import *
from .utils import *
from store.utils import cartData, cookieCartData

import datetime
import json
import requests


MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0'
members_endpoint = f'{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members'

tax_rate = {
    'Ontario': 13,
    'British Columbia': 12,
    'Quebec': 14.975,
    'Alberta': 5,
    'Manitoba': 13,
    'New Brunswick': 13,
    'Newfoundland and Labrador': 13,
    'Northwest Territories': 5,
    'Nova Scotia': 15,
    'Nunavut': 5,
    'Prince Edward Island': 14,
    'Saskatchewan': 10,
    'Yukon': 5
}


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
                if form.cleaned_data['subscription']:
                    subscribe(form.cleaned_data['first_name'] + " " + form.cleaned_data['last_name'],
                              form.cleaned_data['email'])
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
        form = UpdateUserForm(request.POST.copy())
        if form.is_valid() and request.user.is_authenticated:
            if request.user.check_password(form.cleaned_data['cur_password']):
                try:
                    customer = request.user.customer
                    customer.user.first_name = form.cleaned_data['first_name']
                    customer.user.last_name = form.cleaned_data['last_name']
                    customer.phone = form.cleaned_data['phone']
                    customer.name = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
                    if form.cleaned_data['password1'] and form.cleaned_data['password1'] == form.cleaned_data['password2']:
                        password = form.cleaned_data['password2']
                        try:
                            password_validation.validate_password(password)
                            customer.user.set_password(password)
                            customer.save()
                            customer.user.save()
                            messages.success(request, 'Account information changed')
                        except:
                            messages.error(request, """Invalid Password:
                                            Your password can’t be too similar to your other personal information. 
                                            Your password must contain at least 8 characters. 
                                            Your password can’t be a commonly used password.
                                            Your password can’t be entirely numeric.""")
                    elif form.cleaned_data['password1']:
                        messages.error(request, 'Passwords do not match')
                    else:
                        customer.save()
                        customer.user.save()
                        messages.success(request, 'Account information changed')
                except:
                    messages.error(request, 'Unable to change information')
            else:
                messages.error(request, 'Please Confirm Current Password to Make Changes')
        else:
            messages.error(request, 'Unable to change information: Please confirm current password')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def subscribe(name, email):
    flname = name.split(' ')
    fname = str(flname[0])
    lname = ""
    for name in flname[1:]:
        lname += " " + str(name)
    lname.strip()

    data = {
        "email_address": email,
        "status": "subscribed",
        "merge_fields": {
            "FNAME": fname,
            "LNAME": lname,
        }
    }
    r = requests.post(
        members_endpoint,
        auth=("", MAILCHIMP_API_KEY),
        data=json.dumps(data)
    )
    return r.status_code, r.json()


def email_list_signup(request):
    form = EmailSignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            subscriber, created = EmailSignup.objects.get_or_create(email=form.cleaned_data['email'])
            subscriber.name = form.cleaned_data['name']
            if request.user.is_authenticated and subscriber.email == request.user.email:
                try:
                    subscriber.user = request.user
                except:
                    messages.error(request, "Already subscribed")
            subscribe(form.instance.name, form.instance.email)
            subscriber.save()
            messages.success(request, "Subscription Successful!")
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
        province = data['shipping']['province']
        if data['shipping']['country'] == 'Canada':
            order.shipping_cost = 15
            try:
                order.tax = tax_rate[province]
            except:
                print('not working')
                messages.error(request, 'Please select a province in Canada')
                return JsonResponse("error", safe=False)
        elif data['shipping']['country'] == 'USA':
            order.shipping_cost = 30
            order.tax = None
        else:
            order.shipping_cost = 50
    else:
        order.tax = 13


    if data['is_layaway']:
        order.layaway = True
    order.save()

    order_data = {
        'delivery': order.delivery,
        'shipping_cost': order.shipping_cost,
        'tax': order.tax,
        'tax_total': order.get_tax_total,
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
        order.status = "In Progress"
    order.save()

    if 'code' in request.session:
        del request.session['code']

    # decrease product quantity according to order details
    for item in order.orderitem_set.all():
        item.product.quantity -= item.quantity
        if item.product.quantity <= 0:
            item.product.in_stock = False
        item.product.save()

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

    order_data = {
        'transaction_id': order.transaction_id,
    }
    return JsonResponse(order_data)


def account(request):
    context = {
    }
    return render(request, 'user/account.html')


def editAddress(request, id):
    if request.method == 'POST':
        try:
            address = request.POST.get('address')
            address2 = request.POST.get('address2')
            city = request.POST.get('city')
            province = request.POST.get('province')
            country = request.POST.get('country')
            postal_code = request.POST.get('postal_code')
            print(address)
            print(postal_code)
            shippingAddress = get_object_or_404(ShippingAddress, id=id)
            shippingAddress.address = address
            shippingAddress.address2 = address2
            shippingAddress.city = city
            shippingAddress.province = province
            shippingAddress.country = country
            shippingAddress.postal_code = postal_code
            shippingAddress.save()
            messages.success(request, 'Account information changed')
        except:
            messages.error(request, 'Unable to change information')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def removeAddress(request, id):
    address = get_object_or_404(ShippingAddress, id=id)
    customer = address.customer.name
    if request.user.is_authenticated and request.user.customer.name == customer:
        address.delete()
        messages.success(request, f'"{address}" has been successfully removed from your account')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
