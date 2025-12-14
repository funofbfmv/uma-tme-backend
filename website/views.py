from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SiteSettings, ServiceCategory, Lead
from .serializers import (
    SiteSettingsSerializer,
    ServiceCategorySerializer,
    LeadSerializer,
)


class SiteSettingsView(APIView):
    def get(self, request):
        settings_obj = SiteSettings.objects.first()
        if not settings_obj:
            return Response({})
        serializer = SiteSettingsSerializer(settings_obj)
        return Response(serializer.data)


class ServiceCategoryListView(generics.ListAPIView):
    queryset = ServiceCategory.objects.prefetch_related("services").all()
    serializer_class = ServiceCategorySerializer


class LeadCreateView(generics.CreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
