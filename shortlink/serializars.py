from rest_framework import serializers
from shortlink.models import ShortLink


class ShortLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortLink
        fields = ('id', 'url', 'short_url', 'time_stamp', 'quantity', 'is_active')
