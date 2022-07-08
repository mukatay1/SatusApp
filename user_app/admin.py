from django.contrib import admin
from .models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'name',
        'surname',
        'birth',
        'gender',
        'phone',
        'city',
        'time_created'
    )
    list_filter = (
        'gender',
        'city'
    )
    search_fields = (
        'user',
        'name',
        'surname'
    )
    prepopulated_fields = {
        "slug": (
            "name",
        )
    }
