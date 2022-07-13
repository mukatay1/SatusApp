from rest_framework import serializers

from .models import Targets


class TargetsSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(
        read_only=True
    )

    class Meta:
        model = Targets
        fields = (
            'name',
            'user',
            'parent',
            'is_completed',
        )

    def get_name(self, obj):
        return 'Mr ' + obj.name
