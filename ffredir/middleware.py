from django.conf import settings
import urllib
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect
from django.contrib.redirects.middleware import RedirectFallbackMiddleware


class RedirectTempFallbackMiddleware(RedirectFallbackMiddleware):
    response_redirect_class = HttpResponseRedirect
    response_gone_class = HttpResponseRedirect

class SetDynamicSites(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # print(repr(request.META))

        try:
            domainname = request.META['HTTP_HOST'].split(':')
            current_site = Site.objects.get(domain=domainname[0])
            settings.SITE_ID._set(current_site.id)
            # print("Set site id to {}".format(settings.SITE_ID))
        except Exception as e:
            #print("Set site id to default due to {}".format(repr(e)))
            settings.SITE_ID._set(1)
        return self.get_response(request)
