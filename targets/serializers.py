from rest_framework import serializers

from .models import Targets


class TargetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Targets
        fields = (
            'name',
            'user',
            'parent',
            'is_completed',
        )
