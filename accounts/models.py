from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils.functional import cached_property


from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import CustomUserManager

# Create your models here.


class UserGroup(Group):
    class Meta:
        proxy = True
        verbose_name = _("User Group")
        verbose_name_plural = _("User Groups")


class User(AbstractUser):
    """
    This model contains the very basic and commonly used data of any user logged in, into the system. You can modify it as per your needs.
    """

    first_name = None
    last_name = None

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    full_name = models.CharField(_("Full name"), max_length=255, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(_("Email address"), null=True, blank=True)
    mobile = PhoneNumberField(_("Phone number"), null=True, blank=True)
    photo = models.ImageField(upload_to="profile_pics", blank=True, null=True)

    is_email_verified = models.BooleanField(
        default=False, help_text=_("Check to verify user's email.")
    )
    is_mobile_verified = models.BooleanField(
        default=False, help_text=_("Check to verify user's phone number.")
    )

    # Meta
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()

        # Check if 'email' is unique
        if self.email:
            if User.objects.filter(email=self.email).exclude(id=self.id).exists():
                raise ValidationError(
                    _("Email address must be unique"),
                    code="unique",
                )

        # Check if 'mobile' is unique
        if self.mobile:
            if User.objects.filter(mobile=self.mobile).exclude(id=self.id).exists():
                raise ValidationError(
                    _("Phone number must be unique"),
                    code="unique",
                )

    @cached_property
    def is_belongs_to_support_team(self):
        if self.is_superuser:
            return True
        return self.groups.filter(name__exact="support").exists()

    @cached_property
    def avatar_url(self):
        if self.photo:
            return self.photo.url
        return "https://img.icons8.com/material-outlined/256/null/user--v1.png"

    @cached_property
    def mobile_number(self):
        return self.mobile.as_e164 if self.mobile else None
