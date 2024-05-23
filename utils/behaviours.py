import uuid as uuid
from django.db import models

from django.conf import settings
from django.core.validators import RegexValidator
from django.utils import timezone
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from .managers import StatusMixinManager
from .utils import upload_location, validator_ascii, validator_pan_no


class StatusMixin(models.Model):
    is_active = models.BooleanField(default=True, blank=False, null=False)
    is_deleted = models.BooleanField(default=False, blank=False, null=False)

    objects = StatusMixinManager()

    def activate(self):
        if not self.is_active:
            self.is_active = True
            self.save()

    def deactivate(self):
        if self.is_active:
            self.is_active = False
            self.save()

    def remove(self):
        if not self.is_deleted:
            self.is_deleted = True
            self.save()

    def has_changed(self, field):
        model = self.__class__.__name__
        return getattr(self, field) != getattr(
            self, "_" + model + "__original_" + field
        )

    def save(self, *args, **kwargs):
        """
        Makes sure that the ``is_active`` is ``False`` when ``is_deleted`` is ``True``.
        """
        if self.is_deleted:
            self.is_active = False
        super(StatusMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class EmailMixin(models.Model):
    email = models.EmailField(max_length=70, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        abstract = True

class MobileMixin(models.Model):
    mobile = models.CharField(
        blank=True,
        null=True,
        max_length=10,
        help_text="Enter a valid 10 digit mobile number.",
    )
    country_code = models.CharField(
        blank=True,
        null=True,
        max_length=5,
        help_text="Enter a valid country code.",
    )

    class Meta:
        abstract = True


class UUIDMixin(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        abstract = True


class UserStampedMixin(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name="created_%(class)s",
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name="updated_%(class)s",
    )

    class Meta:
        abstract = True


class ImageMixin(models.Model):
    image = models.ImageField(_("image"), upload_to=upload_location, null=True, blank=True)
    image_alt = models.CharField(_("image alt"), max_length=100, blank=True, validators=[validator_ascii])

    class Meta:
        abstract = True
