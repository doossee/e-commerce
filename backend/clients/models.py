import uuid
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from .managers import CustomUserManager
from django.core.validators import RegexValidator, validate_email

phone_regex = RegexValidator(
    regex=r'^\+\d{12}$', message='Wrong  number'
)

class CustomUser(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(max_length=255, unique=True, blank=True, null=True, validators=[validate_email])
    email_verified = models.BooleanField(default=False)

    mobile = models.CharField(validators=[phone_regex], max_length=17, unique=True, blank=True, null=True)
    mobile_verified = models.BooleanField(default=False)
    
    username = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "mobile"
    REQUIRED_FIELDS = ["username"]

    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return self.mobile

