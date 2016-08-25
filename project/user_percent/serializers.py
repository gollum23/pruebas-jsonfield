from rest_framework import serializers

from .models import UserPercent


class UserPercentSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPercent
        fields = (
            'pk',
            'user_id',
            'courses'
        )