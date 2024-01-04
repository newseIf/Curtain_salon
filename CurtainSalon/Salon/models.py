from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Discounts(models.Model):
    discount_id = models.AutoField(primary_key=True)
    name_discount = models.CharField(blank=True, max_length=100, verbose_name='Название скидки')
    percent = models.IntegerField(blank=True,verbose_name='Процент')

    class Meta:
        managed = False
        db_table = 'discounts'
        verbose_name = "Скидки"
        verbose_name_plural = "Скидки"

    def __str__(self):
        return f"{self.name_discount}: {self.percent}"


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('Users', models.DO_NOTHING, verbose_name='Продавец')
    structure_delivery = models.ForeignKey('StructureDelivery', models.DO_NOTHING, verbose_name='Поставка')

    class Meta:
        managed = False
        db_table = 'inventory'
        verbose_name = "Инвентаризация"
        verbose_name_plural = "Инвентаризация"

    def __str__(self):
        return f"{self.user} - {self.structure_delivery}"


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    date_order = models.DateField(verbose_name='Дата заказа')
    status_order = models.BooleanField(verbose_name='Статус заказа')
    total_cost = models.FloatField(verbose_name='Общая стоимость')
    product = models.ForeignKey('Product', models.DO_NOTHING, verbose_name='Продукция')
    service = models.ForeignKey('Services', models.DO_NOTHING, verbose_name='Услуги')

    class Meta:
        managed = False
        db_table = 'orders'
        verbose_name = "Заказы"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"{self.date_order} - {self.product}, {self.total_cost}"


class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    name_post = models.CharField(blank=True, max_length=50, verbose_name='Должность')
    salary = models.IntegerField(blank=True, verbose_name='Оклад')

    class Meta:
        managed = False
        db_table = 'posts'
        verbose_name = "Должности"
        verbose_name_plural = "Должности"

    def __str__(self):
        return f"{self.name_post}: {self.salary}"


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, max_length=100, verbose_name='Название')
    price = models.IntegerField(blank=True, verbose_name='Цена')
    country_producer = models.CharField(max_length=100, null=True, verbose_name='Страна производитель')
    description = models.CharField(max_length=300, verbose_name='Описание')
    size = models.FloatField(verbose_name='Размер')
    color = models.CharField(blank=True, max_length=50, verbose_name='Цвет')
    photo = models.CharField(blank=True, max_length=255, verbose_name='Фото')
    discount = models.ForeignKey(Discounts, models.DO_NOTHING, blank=True, null=True, verbose_name='Скидка')
    product_type = models.ForeignKey('ProductType', models.DO_NOTHING, verbose_name='Тип продукции')
    slug = models.SlugField(max_length=50, db_index=True)

    class Meta:
        managed = False
        db_table = 'product'
        verbose_name = "Продукция"
        verbose_name_plural = "Продукция"
        # ordering = ('name',)
        # index_together = (('product_id', 'slug'),)

    def __str__(self):
        return f"{self.name} - {self.color},{self.size},{self.price}"

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_id': self.pk})


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'Salon_cartitem'
        verbose_name = "Корзина"
        verbose_name_plural = "Корзина"

    def __str__(self):
        return f'{self.quantity} x {self.product.name}'


class ProductType(models.Model):
    product_type_id = models.AutoField(primary_key=True)
    name_product_type = models.CharField(blank=True, max_length=50, verbose_name='Тип продукции')
    slug = models.SlugField(max_length=50, db_index=True)

    class Meta:
        managed = False
        db_table = 'product_type'
        verbose_name = "Тип продукции"
        verbose_name_plural = "Тип продукции"

    def __str__(self):
        return f"{self.name_product_type}"

    def get_absolute_url(self):
        return reverse('type', kwargs={'type_id': self.pk})


class Roles(models.Model):
    role_id = models.AutoField(primary_key=True)
    name_role = models.CharField(blank=True, max_length=100, verbose_name='Роль')

    class Meta:
        managed = False
        db_table = 'roles'
        verbose_name = "Роли"
        verbose_name_plural = "Роли"

    def __str__(self):
        return f"{self.name_role}"


class Services(models.Model):
    service_id = models.AutoField(primary_key=True)
    name_service = models.CharField(blank=True, max_length=50, verbose_name='Услга')

    class Meta:
        managed = False
        db_table = 'services'
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return f"{self.name_service}"


class StructureDelivery(models.Model):
    structure_delivery_id = models.AutoField(primary_key=True)
    number_products = models.IntegerField(verbose_name='Количество продукции')
    date_delivery = models.DateField(verbose_name='Дата поставки')
    product = models.ForeignKey(Product, models.DO_NOTHING, verbose_name='Продукция')
    user = models.ForeignKey('Users', models.DO_NOTHING, verbose_name='Пользователь')

    class Meta:
        managed = False
        db_table = 'structure_delivery'
        verbose_name = "Состав поставки"
        verbose_name_plural = "Состав поставки"

    def __str__(self):
        return f"{self.user} - {self.date_delivery}, {self.number_products}"


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    surname = models.CharField(blank=True, max_length=50, verbose_name='Фамилия')
    name = models.CharField(blank=True, max_length=50, verbose_name='Имя')
    patronymic = models.CharField(max_length=50, null=True, verbose_name='Отчество')
    date_birth = models.DateField(verbose_name='Дата рождения')
    photo = models.CharField(blank=True, null=True, verbose_name='Фото')
    telephone = models.CharField(max_length=12, verbose_name='Телефон')
    email = models.CharField(max_length=50)
    street = models.CharField(blank=True, max_length=50, verbose_name='Улица')
    house = models.IntegerField(blank=True,verbose_name='Дом')
    floor = models.IntegerField(null=True, verbose_name='Этаж')
    name_company = models.CharField(max_length=50, blank=True, null=True, verbose_name='Назавние компании')
    role = models.ForeignKey(Roles, models.DO_NOTHING, blank=True, verbose_name='Роль')
    post = models.ForeignKey(Posts, models.DO_NOTHING, blank=True, null=True, verbose_name='Должность')
    password = models.CharField(blank=True, verbose_name='Пароль')

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name = "Пользователиcd"
        verbose_name_plural = "Пользователи"

        def __str__(self):
            return f"{self.surname} {self.name} - {self.email}"
