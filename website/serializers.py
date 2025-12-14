from rest_framework import serializers
from .models import SiteSettings, ServiceCategory, Service, Lead


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = [
            "site_name",
            "logo",
            "hero_title",
            "hero_subtitle",
            "phone",
            "email",
            "address",
            "whatsapp_link",
            "telegram_link",
            "footer_text",
        ]


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            "id",
            "title",
            "short_description",
            "full_description",
            "icon",
            "is_featured",
            "order",
            "category",
        ]


class ServiceCategorySerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, read_only=True)

    class Meta:
        model = ServiceCategory
        fields = ["id", "title", "slug", "order", "services"]


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = ["id", "name", "phone", "email", "service", "message", "created_at"]
        read_only_fields = ["created_at"]
