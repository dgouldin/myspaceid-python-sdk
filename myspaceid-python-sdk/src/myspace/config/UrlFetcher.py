
import urllib2

from myspace.config.HTTPResponse import HTTPResponse
    
class UrlFetcher(object):
    def fetch(self, url, body=None, headers=None):
        if headers is None:
            headers = {}
        req = urllib2.Request(url, data=body, headers=headers)
        try:
            f = urllib2.urlopen(req)
            try:
                return self._makeResponse(f)
            finally:
                f.close()
        except urllib2.HTTPError, why:
            try:
                return self._makeResponse(why)
            finally:
                why.close()

    def _makeResponse(self, urllib2_response):
        resp = HTTPResponse()
        resp.body = urllib2_response.read()
        resp.final_url = urllib2_response.geturl()
        resp.headers = dict(urllib2_response.info().items())
    
        if hasattr(urllib2_response, 'code'):
            resp.status = urllib2_response.code
        else:
            resp.status = 200   
        return resp