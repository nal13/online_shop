#
# ref:
#   https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#a-full-example
#

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, shown_name, client_id, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            shown_name=shown_name,
            client_id=client_id,
        )
        user.set_password( password )
        user.save( using=self._db )

        return user

    def create_superuser(self, email, shown_name, client_id, password):
        user = self.create_user(
            email,
            password=password,
            shown_name=shown_name,
            client_id=client_id,
        )
        user.is_admin = True
        user.save( using=self._db )

        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        unique=True,
        max_length=40,
    )
    shown_name = models.CharField( max_length=40 )
    client_id = models.PositiveSmallIntegerField( null=True )
    is_active = models.BooleanField( default=True )
    is_admin = models.BooleanField( default=False )

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['shown_name', ]

    def set_client_id(self, id):
        self.client_id = id
        self.save()
        return True

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
