
#poortablecontact

API_CONTACTS_URL = 'http://api.myspace.com/v2/people/%s/@self'
API_FRIENDCONTACTS_URL = 'http://api.myspace.com/v2/people/%s/@friends'

class PortableContact():

    def __init__(self,objmyspacecontext):
        global context
        context= objmyspacecontext      
     
    """ Portable Contacts REST Resources
        Resource:   http://api.myspace.com/v2/people/@me/@self 
        Description:Person Resource
        Parameters: @person_id (mandatory parameter) current person id e.g: @me
                    @page (optional parameter)  startIndex must be in the form of startIndex = (count * i) + 1,
                    where i is any non-negative integer, 
                    e.g. if count = 5, startIndex can be 1, 6, 11, 16, etc.
                    @pagesize (optional parameter) total number of records                               
        Details:    http://wiki.developer.myspace.com/index.php?title=Portable_Contacts_REST_Resources
    """ 
    def get_personpoco(self,person_id, page=None, page_size=None, fields=None):
        context.validate_params(locals())
        contacts_request_url = API_CONTACTS_URL % person_id
        #set up extra params, if any
        params = {}
        if page is not None:
            params['page'] = page
        if page_size is not None:
            params['page_size'] = page_size
        if fields is not None:
            params['fields'] = fields
    
        return context.callmyspaceapi(contacts_request_url, parameters=params)    
    
    """ Portable Contacts REST Resources
        Resource:   http://api.myspace.com/v2/people/@me/@friends 
        Description:Person Resource
        Parameters: @person_id (mandatory parameter) current person id e.g: @me
                    @page (optional parameter)  startIndex must be in the form of startIndex = (count * i) + 1,
                    where i is any non-negative integer, 
                    e.g. if count = 5, startIndex can be 1, 6, 11, 16, etc.
                    @pagesize (optional parameter) total number of records                               
        Details:    http://wiki.developer.myspace.com/index.php?title=Portable_Contacts_REST_Resources
    """
    def get_friendspoco(self,person_id, page=None, page_size=None):
        context.validate_params(locals())
        friendcontacts_request_url = API_FRIENDCONTACTS_URL % person_id
        #set up extra params, if any
        params = {}
        if page is not None:
            params['page'] = page
        if page_size is not None:
            params['page_size'] = page_size
                   
        return context.callmyspaceapi(friendcontacts_request_url, parameters=params) 