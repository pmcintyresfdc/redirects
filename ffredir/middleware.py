from django.conf import settings
import urllib
from django.contrib.sites.models import Site


class SetDynamicSites(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        try:
            bits = urllib.urlsplit(request.META['HTTP_HOST'])[0].split('.')
            bits = request.META.get('HTTP_HOST', '').split('.')
            domainname = request.META['HTTP_HOST'].split(':')
            current_site = Site.objects.get(domain=domainname[0])
            settings.SITE_ID._set(current_site.id)
        except:
            settings.SITE_ID._set(1)
        return None
