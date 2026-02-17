from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.ReadOnlyField(source='actor.username')
    recipient = serializers.ReadOnlyField(source='recipient.username')

    class Meta:
        model = Notification
        fields = ['id', 'recipient', 'actor', 'verb', 'is_read', 'timestamp']
        read_only_fields = ['id', 'recipient', 'actor', 'verb', 'timestamp']