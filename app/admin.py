from django.contrib import admin

from .models import Order, ConsultationRequest


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display= (
        'id',
        'customer_name',
        'phone',
        'bouquet',
        'delivery_time',
        'status',
        'created_at',
    )
    list_filter = (
        'status',
        'delivery_time',
        'created_at',
    )
    search_fields = (
        'customer_name',
        'phone',
        'address',
        'bouquet__title',
    )
    list_editable = (
        'status',
    )
    readonly_fields = (
        'created_at',
    )

@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer_name',
        'phone',
        'is_processed',
        'created_at',
    )
    list_filter = (
        'is_processed',
        'created_at',
    )
    search_fields = (
        'customer_name',
        'phone',
    )
    list_editable = (
        'ist_processed',
    )
    readonly_fields = (
        'created_at',
    )