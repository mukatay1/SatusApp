from django.contrib import admin
from .models import Targets


@admin.register(Targets)
class TargetsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'user',
        'parent',
        'is_completed',
    )
    list_filter = (
        'user',
        'is_completed',
    )
