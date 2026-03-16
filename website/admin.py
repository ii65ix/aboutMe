from django.contrib import admin

from .models import ContactInfo, PersonalInfo, Service


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ("full_name", "hero_title")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "instagram", "tiktok", "whatsapp_number")
