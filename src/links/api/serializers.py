from rest_framework import serializers
from django.urls import reverse
from links.models import Link


class LinkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    original_url = serializers.URLField()
    short_code = serializers.CharField(read_only=True)
    short_url = serializers.SerializerMethodField()
    clicks = serializers.IntegerField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    def get_short_url(self, obj):
        request = self.context.get('request')
        if request and obj.short_code:
            short_url = reverse('redirect', kwargs={'short_code': obj.short_code})
            return request.build_absolute_uri(short_url)
        return None