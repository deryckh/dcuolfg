# Copyright 2012-2013 Deryck Hodge.  This software is licensed under the
# GNU Lesser General Public License version 3 (see the file LICENSE).

"""Views used in development only."""

import urllib2
from django.http import HttpResponse


def api(request):
    """A view for serving the API in development."""
    url = 'http://127.0.0.1:8077'
    proxy_request = urllib2.Request(url)
    response = urllib2.urlopen(proxy_request)
    return HttpResponse(
        response.read(), mimetype=response.info().getheader('Content-Type'))
