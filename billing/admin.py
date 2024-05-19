from django.contrib import admin
from .models import Billing

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_type', 'comments_text', 'created_date')
    list_display_links = ('id', 'payment_type', 'created_date')
    search_fields = ('id', 'payment_type',)
    list_filter = ('id', 'payment_type',)
    ordering = ('created_date',)

    def comments_text(self, obj):
        return obj.comments[:15]
