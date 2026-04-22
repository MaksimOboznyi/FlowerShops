from django.contrib import admin
from django.utils.html import format_html
from .models import Order, ConsultationRequest, Bouquet, Occasion


@admin.register(Occasion)
class OccasionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

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
        'is_processed',
    )
    readonly_fields = (
        'created_at',
    )


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'occasion',
        'price',
        'is_active',
        'image_preview',
    )
    list_filter = ('is_active', 'occasion')
    search_fields = ('title', 'description', 'composition')
    list_editable = ('price', 'is_active')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'updated_at', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" />', obj.image.url)
        return 'Нет изображения'

    image_preview.short_description = 'Превью'