from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    member_name = models.CharField(db_column='member_name', max_length=100, default='')
    deleted_flag = models.BooleanField(default=False, verbose_name='삭제여부')

    class Meta:
        db_table = "auth_profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class ATMSymbolKraken(models.Model):
    service = models.IntegerField(blank=True, null=True, default=0)
    symbol = models.CharField(db_column="symbol", max_length=255)
    symbol_call = models.CharField(db_column="symbol_call", max_length=255, default='')
    auto_flag = models.CharField(db_column="auto_flag", max_length=10, default='0')
    tr_price = models.DecimalField(max_digits=31, decimal_places=18, default=0)
    tr_qty = models.DecimalField(max_digits=31, decimal_places=18, default=0)
    tr_time = models.BigIntegerField(db_column="tr_time", default=0)
    deleted_flag = models.BooleanField(default=False, verbose_name='사용여부')

    class Meta:
        db_table = "atm_symbol_kraken"
