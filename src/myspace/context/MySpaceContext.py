

import simplejson
import urlparse
from oauthlib import oauth
from myspace.config.UrlFetcher import UrlFetcher
from myspace.config.MySpaceError import MySpaceError

OAUTH_REQUEST_TOKEN_URL = 'http://api.myspace.com/request_token'
OAUTH_AUTHORIZATION_URL = 'http://api.myspace.com/authorize'
OAUTH_ACCESS_TOKEN_URL = 'http://api.myspace.com/access_token'

           
class MySpaceContext():
    
    
    def __init__(self, consumer_key=None, consumer_secret=None, oauth_token_key=None, oauth_token_secret=None):
      self.consumer = oauth.OAuthConsumer(consumer_key, consumer_secret)
      self.signature_method = oauth.OAuthSignatureMethod_HMAC_SHA1()
      if oauth_token_key and oauth_token_secret:
          self.token = oauth.OAuthConsumer(oauth_token_key, oauth_token_secret)
      else:
          self.token = None          
      self.url_fetcher = UrlFetcher() 
      
    """OAuth Related functions 
    """  
    def get_request_token(self):
        resp = self.__call_oauth_api(OAUTH_REQUEST_TOKEN_URL)
        token = oauth.OAuthToken.from_string(resp)       
        return token

    def get_authorization_url(self, token, callback_url):
        oauth_request = oauth.OAuthRequest.from_token_and_callback(
            token=token, callback=callback_url, http_url=OAUTH_AUTHORIZATION_URL
        )
        oauth_request.sign_request(self.signature_method, self.consumer, token)
        return oauth_request.to_url()

    def get_access_token(self, request_token):
        resp = self.__call_oauth_api(OAUTH_ACCESS_TOKEN_URL, token=request_token)
        token = oauth.OAuthToken.from_string(resp)
        
        return token
      
    
    """Miscellaneous utility functions 
    """
    def validate_params(self, params):
        invalid_param = 'Invalid Parameter Value. %s %s'
        # Non empty/None param check
        non_empty_params = ['user_id', 'app_id']
        for param, value in params.items():
            if param in non_empty_params:
                try:
                    user_id = int(value)
                except (ValueError, TypeError):
                    message = invalid_param % (param, ' must be an integer')
                    raise MySpaceError(message)
                    return
        #Non-negative param check
        positive_params = ['page', 'page_size', 'user_id', 'video_id', 'photo_id', 'album_id', 'mood']
        for param, value in params.items():
            if param in positive_params and value is not None:
                if value < 0:
                    message = invalid_param % (param, ' cannot be negative')
                    raise MySpaceError(message)
                    return
        
    def __call_oauth_api(self, oauth_url, token=None, debug=False):
        oauth_request = oauth.OAuthRequest.from_consumer_and_token(
            self.consumer, token=token, http_url=oauth_url
        )
        oauth_request.sign_request(self.signature_method, self.consumer, token)
        resp = self.url_fetcher.fetch(oauth_request.to_url())
        if resp.status != 200:
            raise MySpaceError('MySpace OAuth API returned an error', resp)
        return resp.body 
      
    #def __call_myspace_api(self, api_url, method='GET', parameters=None, debug=False, get_raw_response=False, body=None):      
    def callmyspaceapi(self, api_url, method='GET', parameters=None, debug=False, get_raw_response=False, body=None,flag=None):
        access_token = self.token
        
        
        # Use POST for PUT as well. Set up http_method correctly for base string generation + signing
        http_method = 'POST' if (method == 'POST' or method == 'PUT') else method
        oauth_request = oauth.OAuthRequest.from_consumer_and_token(
            self.consumer, token=access_token, http_method=http_method, http_url=api_url, parameters=parameters
        )
        oauth_request.sign_request(self.signature_method, self.consumer, access_token)

        headers = {}
        #body = None
        if (method == 'PUT'):
            headers['X-HTTP-Method-Override'] = 'PUT'      
        
        if (method == 'POST' and flag == 'image'):
            headers['Content-type'] = 'image/jpeg'    
        
        if (method == 'POST' and flag == 'video'):
            headers['Content-type'] = 'video/mpeg' 
            
        # Generate POST/PUT body
        if (body is not None and flag is None):
            if (method == 'PUT' or method == 'POST' ):
                body += '&'.join('%s=%s' % (oauth.escape(str(k)), oauth.escape(str(v))) for k, v in parameters.iteritems())           
       
        """Get the request URL. For GET it's oauth_request.to_url(). For POST/PUT the URL should have just the oauth
           related params in the query string. Any request specific params go into the POST body - this is due to the
           way MySpace implements it's oauth
        """       
        request_url = oauth_request.to_url()
        if (method == 'POST' or method == 'PUT' ):
            qs = urlparse.urlparse(oauth_request.to_url())[4]
            qparams = oauth_request._split_url_string(qs)
            qs = '&'.join('%s=%s' % (oauth.escape(str(k)), oauth.escape(str(v))) for k, v in qparams.iteritems())
            request_url = oauth_request.get_normalized_http_url() + '?' + qs
            
        resp = self.url_fetcher.fetch(request_url, body=body, headers=headers)
        if resp.status > 201:
            raise MySpaceError('MySpace REST API returned an error', resp)
        api_response = resp.body if get_raw_response else simplejson.loads(resp.body)        
        return api_response
    
    
    
    
