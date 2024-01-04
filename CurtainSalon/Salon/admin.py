from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


class DiscountsAdmin(admin.ModelAdmin):
    list_display = ('discount_id', 'name_discount', 'percent')


class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_id', 'user', 'structure_delivery')


class PostsAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'name_post', 'salary')


class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('product_type_id', 'name_product_type', 'slug')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'price', 'country_producer', 'description', 'size', 'color', 'photo', 'slug')


class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'date_order', 'status_order', 'total_cost', 'product', 'service')


class RolesAdmin(admin.ModelAdmin):
    list_display = ('role_id', 'name_role')


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'name_service')


class StructureDeliveryAdmin(admin.ModelAdmin):
    list_display = ('structure_delivery_id', 'number_products', 'date_delivery', 'product', 'user')


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', )

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'user', 'date_added')


admin.site.register(Users, UserAdmin)
admin.site.register(Discounts, DiscountsAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(StructureDelivery, StructureDeliveryAdmin)
admin.site.register(CartItem, CartAdmin)


