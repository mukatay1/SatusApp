from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify

User = get_user_model()


# Create your models here.
class UserProfile(models.Model):
    CITY = [
        ('nur-sultan', 'Nur-Sultan')
    ]
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('none', 'None')
    ]
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True

    )
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    surname = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    birth = models.DateField(
        blank=True,
        null=True
    )
    gender = models.CharField(
        max_length=6,
        choices=GENDER,
        default='none'
    )
    phone = models.CharField(
        max_length=11,
        blank=True,
        null=True
    )
    image = CloudinaryField(
        'image',
        blank=True
    )
    city = models.CharField(
        max_length=20,
        choices=CITY,
        default='nur-sultan'
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
    )
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.user))
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'
