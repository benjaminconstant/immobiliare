from django.contrib import admin
from .models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    ordering = ['price']
    search_fields = ['title', 'text', 'id', 'link']
    list_display = ['title', 'mq', 'price', 'price_mq', 'costs']

    readonly_fields = ['created', 'updated']
