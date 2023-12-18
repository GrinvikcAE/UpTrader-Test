from django.contrib import admin
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ['name', 'parent']
    ordering = ['name', 'parent']
    list_filter = ['parent']


admin.site.register(Menu, MenuAdmin)
