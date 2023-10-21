from django.contrib import admin
from django.db import models

from solo.admin import SingletonModelAdmin
from ckeditor.widgets import CKEditorWidget

from settings.models import (
    Setting,
    GeneralInformation,
    SocialLink,
)

# Register your models here.


class SocialLinkInline(admin.StackedInline):
    model = SocialLink
    min_num = 0
    extra = 0


@admin.register(Setting)
class SettingAdmin(SingletonModelAdmin):
    inlines = (SocialLinkInline,)
    formfield_overrides = {models.TextField: {"widget": CKEditorWidget}}


@admin.register(GeneralInformation)
class GeneralInformationAdmin(SingletonModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": CKEditorWidget},
    }
