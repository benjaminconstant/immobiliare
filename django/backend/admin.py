from django.contrib import admin
from .models import House, Search


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    ordering = ['price']
    search_fields = ['title', 'text', 'id', 'link']
    list_display = ['date_publish', 'title', 'mq', 'price', 'price_mq', 'costs']
    list_filter = ('search',)
    readonly_fields = ['created', 'updated']


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name', 'link']
    list_display = ['name', 'link']

    readonly_fields = ['created', 'updated']
