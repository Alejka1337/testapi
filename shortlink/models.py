from django.db import models
from django.contrib.auth.models import User


class ShortLink(models.Model):
    url = models.CharField(max_length=128)
    short_url = models.CharField(max_length=128, unique=True)
    time_stamp = models.DateTimeField(null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    ip_address = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'shortlink'
        verbose_name_plural = 'shortlinks'

    def __str__(self):
        return f'Коротка ссылка для {self.url} – {self.short_url}'
