from django.db import models


class Account(models.Model):
    first_name = models.TextField(default=None, null=True, blank=True)
    last_name = models.TextField(default=None, null=True, blank=True)
    email = models.TextField(default=None)
    password = models.TextField(default=None)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'