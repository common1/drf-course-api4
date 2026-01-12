from django.contrib import admin

from .models import (
    User,
    Product,
    Order,
    OrderItem
)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline
    ]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass


