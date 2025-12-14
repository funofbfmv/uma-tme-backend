from django.urls import path
from .views import SiteSettingsView, ServiceCategoryListView, LeadCreateView

urlpatterns = [
    path("settings/", SiteSettingsView.as_view(), name="site-settings"),
    path("service-categories/", ServiceCategoryListView.as_view(), name="service-categories"),
    path("leads/", LeadCreateView.as_view(), name="lead-create"),
]
