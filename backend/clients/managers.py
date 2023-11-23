from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, mobile, email=None, password=None, **extra_fields):
        if not mobile:
            raise ValueError("User must have an mobile")
        email = self.normalize_email(email)
        user = self.model(mobile=mobile, username=mobile, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile, email=None, password=None, **extra_fields):
        user = self.create_user(mobile, email, password=password, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user
