from rest_framework import serializers

from links.models import Link


class LinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Link
        fields = ('id', 'original_url', 'short_code', 'clicks', 'created_at', 'is_active')
        read_only_fields = ('short_code', 'clicks', 'created_at',)
