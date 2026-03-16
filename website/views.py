from django.shortcuts import render
from django.utils.translation import gettext as _

from .models import ContactInfo, PersonalInfo, Service


def _get_personal_info():
    personal = PersonalInfo.objects.first()
    if personal:
        return personal
    return {
        "full_name": "Your Name",
        "hero_title": _("Ready for your project? We build it into a professional app or website"),
        "hero_description": _(
            "I deliver and sell mobile app and web projects, with full support from idea to handoff."
        ),
        "biography": (
            _("I build ready-made and custom digital solutions for clients and students.")
        ),
        "experience": (
            _("My experience includes mobile apps, professional websites, and full project delivery.")
        ),
        "mission": (
            _("My mission is fast, high-quality delivery with clear communication and real results.")
        ),
    }


def _get_contact_info():
    contact = ContactInfo.objects.first()
    if contact:
        return contact
    return {
        "phone_number": "+965 5575 5234",
        "instagram": "codemashro3",
        "tiktok": "codemashro3",
        "whatsapp_number": "+965 5575 5234",
        "whatsapp_link": "96555755234",
    }


def home(request):
    personal = _get_personal_info()
    contact = _get_contact_info()
    return render(request, "website/home.html", {"personal": personal, "contact": contact})


def about(request):
    personal = _get_personal_info()
    return render(request, "website/about.html", {"personal": personal})


def services(request):
    services_list = list(Service.objects.all())
    if not services_list:
        services_list = [
            {
                "title": _("Mobile app project delivery"),
                "description": (
                    _("Professional apps delivered from idea to launch-ready build.")
                ),
            },
            {
                "title": _("Web project delivery"),
                "description": (
                    _("Modern, responsive websites with polished user experience.")
                ),
            },
            {
                "title": _("Ready-made and custom projects"),
                "description": (
                    _("Complete projects tailored and delivered to your requirements.")
                ),
            },
        ]
    return render(request, "website/services.html", {"services": services_list})


def contact(request):
    contact_info = _get_contact_info()
    return render(request, "website/contact.html", {"contact": contact_info})
