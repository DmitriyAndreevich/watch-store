from django.contrib import admin
from .models import *


class CurrencyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Currency._meta.fields]

    class Meta:
        model = Currency


admin.site.register(Currency, CurrencyAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.fields]

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class SliderImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SliderImage._meta.fields]

    class Meta:
        model = SliderImage


admin.site.register(SliderImage, SliderImageAdmin)


class SubscribersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscribers._meta.fields]

    class Meta:
        model = Subscribers


admin.site.register(Subscribers, SubscribersAdmin)


class ProductCardImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCardImage._meta.fields]

    class Meta:
        model = ProductCardImage


admin.site.register(ProductCardImage, ProductCardImageAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contact._meta.fields]

    class Meta:
        model = Contact


admin.site.register(Contact, ContactAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


admin.site.register(Status, StatusAdmin)


