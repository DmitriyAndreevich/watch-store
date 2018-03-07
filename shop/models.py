from django.db import models

class Currency(models.Model):
    currency_name = models.CharField(max_length=12)
    currency_rate = models.DecimalField(max_digits=12, decimal_places=3)
    currency_simbol = models.CharField(max_length=12)

    def __str__(self):
        return " %s" % self.currency_name

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'



class Product(models.Model):
    product_name = models.CharField(max_length=128, blank=True, default=None)
    product_description = models.TextField(max_length=256, blank=True, null=True, default=None)
    is_exists = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    product_image = models.ImageField(null=True, upload_to = 'products_images/')
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    discount_product = models.IntegerField(blank=True, null=True, default=None)
    product_full_description = models.TextField(max_length=1024, blank=True, null=True, default=None)
    product_addition_inf = models.TextField(max_length=1024, blank=True, null=True, default=None)

    def __str__(self):
        return " %s" % self.product_name


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Category(models.Model):
    category_name = models.CharField(max_length=128, blank=True, default=None)

    def __str__(self):
        return " %s" % self.category_name


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'




class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "Статус %s" % self.name

        class Meta:
            verbose_name = 'Статус заказа'
            verbose_name_plural = 'Статусы заказа'

class Order(models.Model):
    customer_name = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_email = models.EmailField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    comments = models.TextField(max_length=256, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s  %s" % (self.id, self.customer_name)

        class Meta:
        	verbose_name = 'Заказ'
        	verbose_name_plural = 'Заказы'




class SliderImage(models.Model):
    slider_image = models.ImageField(null=True, upload_to = 'products_images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return " %s" % self.slider_image

    class Meta:
        verbose_name = 'SliderImage'
        verbose_name_plural = 'Slider_images'



class Subscribers(models.Model):
	email = models.EmailField()


	class Meta:
		verbose_name = 'Subscriber'
		verbose_name_plural = 'Subscribers'



class ProductCardImage(models.Model):
	product = models.ForeignKey(Product, blank=True, null=True, default=None)
	card_image = models.ImageField(null=True, upload_to = 'products_images/')
	is_active = models.BooleanField(default=True)

	def __str__(self):
		return " %s" % self.card_image

	class Meta:
		verbose_name = 'ProductCardImage'
		verbose_name_plural = 'ProductCardImages'


class Contact (models.Model):
	your_name = models.CharField(max_length=255)
	your_email = models.EmailField(max_length=75)
	your_phone = models.CharField(max_length=255)
	your_message = models.TextField()




class Checkout (models.Model):
	your_name = models.CharField(max_length=255)
	your_email = models.EmailField(max_length=75)
	your_phone = models.CharField(max_length=255)
	your_message = models.TextField()

