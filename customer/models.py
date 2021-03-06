from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from rest_framework.authtoken.models import Token

from customer.manager import UserManager
from customer.model_validator import validate_mobile
from address.models import Address


class User(AbstractBaseUser, PermissionsMixin):
    mobile = models.BigIntegerField(_('mobile number'), unique=True, validators=[validate_mobile])
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(
        _('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.')
    )
    address = models.ManyToManyField(Address, related_name='user', through='UserToAddress', blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'mobile'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_username(self):
        """Return the username for this User."""
        return str(getattr(self, self.USERNAME_FIELD))

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name


@receiver(post_save, sender=User)
def make_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


class UserToAddress(models.Model):
    """
    Model represent the M:M relation within user and Address
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Address User')
        verbose_name_plural = _('Address Users')
        unique_together = ('user', 'address',)

    def __str__(self):
        return str(self.user.mobile) + ' ' + self.address.area_house_number
