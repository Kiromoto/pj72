from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


# Товар для нашей витрины
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products')
    price = models.FloatField(validators=[MinValueValidator(0.0)])


    def __str__(self):
        return f'{self.name()}: {self.description[:20]}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


# Категория, к которой будет привязываться товар
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class Order(models.Model):  # наследуемся от класса Model
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='ProductOrder')

class Staff(models.Model):
    director = 'DI'
    admin = 'AD'
    cook = 'CO'
    cashier = 'CA'
    cleaner = 'CL'

    POSITIONS = [
        (director, 'Директор'),
        (admin, 'Администратор'),
        (cook, 'Повар'),
        (cashier, 'Кассир'),
        (cleaner, 'Уборщик')
    ]

    position = models.CharField(max_length=2, choices=POSITIONS, default=cashier)
    full_name = models.CharField(max_length = 255)
    labor_contract = models.IntegerField()


class ProductOrder(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    pickup = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def product_sum(self):
        product_price = self.product.price
        return product_price * self.amount
