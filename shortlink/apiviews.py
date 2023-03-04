from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
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


class DetailShortLink(RetrieveAPIView):
    serializer_class = ShortLinkSerializer
    lookup_field = 'id'

    def get_queryset(self):
        if self.request.user.is_anonymous:
            queryset = ShortLink.objects.filter(ip_address=self.request.META['REMOTE_ADDR'], is_active=True)
        else:
            queryset = ShortLink.objects.filter(user=self.request.user, is_active=True)
        return queryset


class UpdateShortLink(UpdateAPIView):
    serializer_class = ShortLinkSerializer
    queryset = ShortLink.objects.all()

    def get_object(self):

        if self.request.user.is_anonymous:
            current_shortlink = ShortLink.objects.get(
                id=self.kwargs.get('id'),
                ip_address=self.request.META['REMOTE_ADDR']
            )

        else:
            current_shortlink = ShortLink.objects.get(
                id=self.kwargs.get('id'),
                user=self.request.user
            )
        return current_shortlink

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.is_active = False
        obj.save()
        return Response({'status': 'success'})
