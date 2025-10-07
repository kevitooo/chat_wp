from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("whatsapp/webhook/", views.whatsapp_webhook, name="whatsapp_webhook"),
]
