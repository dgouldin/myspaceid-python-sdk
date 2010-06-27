
class HTTPResponse(object):
    headers = None
    status = None
    body = None
    final_url = None
    
    def __init__(self, final_url=None, status=None, headers=None, body=None):
        self.final_url = final_url
        self.status = status
        self.headers = headers
        self.body = body
    
    def __repr__(self):
        return "[HTTP Status Code: %r --- Request URL: %s --- Response: %s" % (self.status, self.final_url, self.body)
