from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from shop.forms import OrderForm
from .models import Currency, Product, Category, SliderImage, Subscribers, ProductCardImage, Contact, Order, Status
from .forms import SubscriberForm
from .forms import ContactForm
from django.contrib import messages


def index(request):
    currencies = Currency.objects.all()
    best_products = Product.objects.filter(is_bestseller=True)[:3]
    exists_products = Product.objects.filter(is_exists=True)[:8]
    categories = Category.objects.all()
    slider_images = SliderImage.objects.all()
    card_image = ProductCardImage.objects.all()

    if 'cart' not in request.session:
        request.session['cart'] = list()
    cart_products = Product.objects.filter(id__in=request.session['cart'])
    cart_total_price = 0
    for product in cart_products:
        cart_total_price = cart_total_price + product.product_price

    return render(request, 'index.html', locals())


def product_card(request, id):  # поменял pk на id
    product = get_object_or_404(Product, id=id)
    images = ProductCardImage.objects.filter(is_active=True, product=product)
    exists_products = Product.objects.filter(is_exists=True)[:4]
    currencies = Currency.objects.all()
    categories = Category.objects.all()
    card_image = ProductCardImage.objects.all()

    if 'cart' not in request.session:
        request.session['cart'] = list()
    cart_products = Product.objects.filter(id__in=request.session['cart'])
    cart_total_price = 0
    for product in cart_products:
        cart_total_price = cart_total_price + product.product_price

    return render(request, 'product_card.html', locals())


def contact(request):
    currencies = Currency.objects.all()
    categories = Category.objects.all()

    if 'cart' not in request.session:
        request.session['cart'] = list()
    cart_products = Product.objects.filter(id__in=request.session['cart'])
    cart_total_price = 0
    for product in cart_products:
        cart_total_price = cart_total_price + product.product_price
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            result = form.save()
            print('form saved')
            messages.success(request, "Отлично! Ваши данные приняты!")
        else:
            messages.warning(request, "Упс! Что-то пошло не так!")
    return render(request, 'contact.html', locals())


def subscribe(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            result = form.save()
            messages.success(request, "Отлично! Вы подписаны!")
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.warning(request, "Упс! Что-то пошло не так!")
            return redirect(request.META.get('HTTP_REFERER'))


def add_to_cart(request, id):
    if 'cart' not in request.session:
        request.session['cart'] = list()
    request.session['cart'].append(int(id))
    print(request.session['cart'])
    request.session.modified = True
    messages.success(request, "Отлично! товар добавлен в корзину!")
    return redirect(request.META.get('HTTP_REFERER'))


def checkout(request):
    if 'cart' not in request.session:
        request.session['cart'] = list()
    currencies = Currency.objects.all()
    categories = Category.objects.all()
    cart_products = Product.objects.filter(id__in=request.session['cart'])
    cart_total_price = 0  # Присвоение значения для переменной (local variable referenced before assignment)
    for product in cart_products:
        cart_total_price = cart_total_price + product.product_price

    return render(request, 'checkout.html', locals())


def remove_from_cart(request, id):
    if 'cart' not in request.session:
        request.session['cart'] = list()
    request.session['cart'].remove(int(id))
    request.session.modified = True
    messages.success(request, "Товар успешно удален!")
    return redirect(request.META.get('HTTP_REFERER'))


def remove_cart(request):
    del request.session['cart']
    request.session.modified = True
    return redirect(request.META.get('HTTP_REFERER'))


def order_detail(request):
    currencies = Currency.objects.all()
    categories = Category.objects.all()

    if 'cart' not in request.session:
        request.session['cart'] = list()
    cart_products = Product.objects.filter(id__in=request.session['cart'])
    cart_total_price = 0
    for product in cart_products:
        cart_total_price = cart_total_price + product.product_price
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order1 = form.save()
            print('form saved')
            order1.product.add()
            body = render_to_string("email.html", locals(), request)
            email = EmailMessage('Subject', body, to=['nurixkg@gmail.com'])
            email.content_subtype = 'html'
            email.send()
            messages.success(request, "Отлично! Ваше письмо отправлено!")
        else:
            messages.warning(request, "Упс! Проверьте заполнение полей!")
    else:
        form = OrderForm()

    return render(request, 'order_form.html', locals())


def watches(request, id):
    currencies = Currency.objects.all()
    categories = Category.objects.all()
    exists_products = Product.objects.filter(categories=id)
    categories = Category.objects.all()
    slider_images = SliderImage.objects.all()
    card_image = ProductCardImage.objects.all()
    if 'cart' not in request.session:
        request.session['cart'] = list()
    cart_products = Product.objects.filter(id__in=request.session['cart'])
    cart_total_price = 0
    for product in cart_products:
        cart_total_price = cart_total_price + product.product_price

    return render(request, 'watches.html', locals())