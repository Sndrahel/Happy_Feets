from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number', 'date',
        'total', 'delivery_cost',
        'order_total', 'original_bag', 'stripe_pid',)

    fields = (
        'order_number', 'user_profile', 'date', 'full_name',
        'email', 'phone_number', 'street_address1',
        'postcode', 'town_or_city', 'total', 'delivery_cost',
        'order_total', 'original_bag', 'stripe_pid',)

    list_display = (
        'order_number', 'date', 'full_name',
        'total', 'delivery_cost', 'order_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
