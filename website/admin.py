from django.contrib import admin
from .models import SiteSettings, ServiceCategory, Service, Lead


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)


class ServiceInline(admin.TabularInline):
    model = Service
    extra = 1


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    inlines = [ServiceInline]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "order", "is_featured")
    list_filter = ("category", "is_featured")
    search_fields = ("title", "short_description")


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "service", "created_at", "is_processed")
    list_filter = ("is_processed", "service")
    search_fields = ("name", "phone", "email", "message")
    readonly_fields = ("created_at",)
