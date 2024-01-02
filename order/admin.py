from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name' , 'get_total_cost', 'phone_number', 'paid',
                    'created', 'updated' , 'display_order_items' , 'display_order_slug' , 'latitude', 'longitude' ,'pay_account_user']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]


    def display_order_items(self, obj):
        return ', '.join([f"{item.quantity} x {item.product.name}" for item in obj.items.all()])

    def display_order_slug(self, obj):
        return ', '.join([f"{item.quantity} x {item.product.slug}" for item in obj.items.all()])


    def get_total_cost(self, obj):
        return obj.get_total_cost()
    
    display_order_items.short_description = 'Ordered Items'
    get_total_cost.short_description = 'Total Cost'
    display_order_slug.short_description = 'Ordered slug'
