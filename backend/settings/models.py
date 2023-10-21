from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.functional import cached_property

from solo.models import SingletonModel
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Setting(SingletonModel):
    """
    Settings model
    """

    app_title = models.CharField(max_length=100)
    app_tagline = models.CharField(max_length=100)
    app_logo = models.ImageField(upload_to="logo/", blank=True, null=True)
    app_ios_store_link = models.URLField()
    app_android_store_link = models.URLField()

    # Company Details
    company_address = models.TextField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_address = models.TextField()
    company_mobile = PhoneNumberField("Phone number", null=True, blank=True)
    company_email = models.EmailField()
    company_website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.app_title

    class Meta:
        verbose_name = "Settings"
        verbose_name_plural = "Settings"

    @cached_property
    def social_links(self):
        return self.sociallink_set.all()


class GeneralInformation(SingletonModel):
    app_title = models.CharField(max_length=60, default="Django Boilerplate")
    terms_and_conditions = models.TextField(
        verbose_name=_("Terms & Conditions"), help_text=_("Terms & Conditions")
    )
    privacy_policy = models.TextField(verbose_name=_("Privary Policy"))
    about_us = models.TextField(verbose_name=_("About Us"))

    def __str__(self):
        return "App General Info"

    class Meta:
        verbose_name = _("App General Info")


class SocialLink(models.Model):
    CHOICES = (
        ("facebook", "Facebook"),
        ("twitter", "Twitter"),
        ("youtube", "YouTube"),
        ("linkedin", "LinkedIn"),
        ("telegram", "Telegram"),
        ("whatsapp", "WhatsApp"),
    )
    title = models.CharField(max_length=50, choices=CHOICES, unique=True)
    url = models.URLField(verbose_name=_("Write the Link"))
    settings = models.ForeignKey(Setting, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Social Link"
        verbose_name_plural = "Social Links"
