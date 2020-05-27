from rest_framework import serializers
from home.models import FtUser, ActivityPeriod


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = [
            'start_time',
            'end_time'
        ]
        read_only_fields = ('user',)


class FtUserSerializer(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(many=True)

    class Meta:
        model = FtUser
        fields = [
            "user_id",
            "real_name",
            "tz",
            "activity_periods",
        ]
