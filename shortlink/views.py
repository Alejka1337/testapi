from datetime import datetime
from django.shortcuts import render, redirect

from .utils import create_shortlink
from .models import ShortLink
from shortlink_project.settings import DOMAIN_NAME


def shortlink_index(request):
    if request.method == 'POST':
        url = request.POST['url']
        shortlink = create_shortlink(url)

        if request.user.is_anonymous:
            shortlink_obj = ShortLink(url=url, short_url=shortlink, ip_address=request.META['REMOTE_ADDR'])
            shortlink_obj.save()
        else:
            shortlink_obj = ShortLink(url=url, short_url=shortlink, user=request.user)
            shortlink_obj.save()
        return render(request, 'shortlink/index.html', {'shortlink': shortlink_obj.short_url, 'domain': DOMAIN_NAME})
    return render(request, 'shortlink/index.html')


def redirect_to_url(request, short_link):
    obj = ShortLink.objects.get(short_url=short_link, is_active=True)
    obj.quantity += 1
    obj.time_stamp = datetime.now()
    obj.save()
    return redirect(obj.url)
