from django.contrib import admin

from order.models import Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "budget", "deadline", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("name", "email", "project_description")
    readonly_fields = ("created_at",)

    # відображення полів у формі адміністратора
    fieldsets = (
        ("main", {
            'fields': ('name', 'email', 'project_description', 'budget', 'deadline')
        }),
        ('Status Information', {
            'fields': ('status', 'created_at')
        }),
    )
    ordering = ["-created_at"]
