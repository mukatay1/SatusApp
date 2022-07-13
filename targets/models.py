from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.


class Targets(models.Model):
    name = models.CharField(
        max_length=255,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='user_target',
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='+',
        blank=True,
        null=True,
    )
    is_completed = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.name

    def children(self):
        return Targets.objects.filter(parent=self)
