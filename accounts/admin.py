from django.contrib import admin
from .models import CookieData

@admin.register(CookieData)
class CookieDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
