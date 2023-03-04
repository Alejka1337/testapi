from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from shortlink.serializars import ShortLinkSerializer
from shortlink.models import ShortLink
from shortlink.utils import create_shortlink


class CreateShortLink(CreateAPIView):
    serializer_class = ShortLinkSerializer

    def post(self, request, *args, **kwargs):
        url = request.data.get('url')
        shortlink = create_shortlink(url)

        if request.user.is_anonymous:
            shortlink_obj = ShortLink(url=url, short_url=shortlink, ip_address=request.META['REMOTE_ADDR'])
            shortlink_obj.save()
        else:
            shortlink_obj = ShortLink(url=url, short_url=shortlink, user=request.user)
            shortlink_obj.save()

        return Response(shortlink_obj.short_url, status=status.HTTP_201_CREATED)
