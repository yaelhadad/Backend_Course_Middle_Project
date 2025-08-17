from django.contrib import admin
from .models import Stock, Review

admin.site.register(Stock)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'stock', 'rating', 'created_at']
    list_filter = ['rating', 'created_at', 'stock']
    search_fields = ['user__username', 'stock__symbol', 'comment']
    readonly_fields = ['created_at']
