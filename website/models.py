from django.db import models


class PersonalInfo(models.Model):
    full_name = models.CharField(max_length=120, blank=True)
    hero_title = models.CharField(max_length=200)
    hero_description = models.TextField()
    biography = models.TextField()
    experience = models.TextField()
    mission = models.TextField()

    def __str__(self) -> str:
        return self.full_name or "Personal Info"


class Service(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=40)
    instagram = models.CharField(max_length=120)
    tiktok = models.CharField(max_length=120)
    whatsapp_number = models.CharField(max_length=40)

    def __str__(self) -> str:
        return "Contact Info"

    @property
    def whatsapp_link(self) -> str:
        digits_only = "".join(char for char in self.whatsapp_number if char.isdigit())
        return digits_only