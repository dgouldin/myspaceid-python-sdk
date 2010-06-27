
from myspace.config.MySpaceError import MySpaceError
#OPEN SOCIAL VERSION 0.9 

API_OPENSOCIAL_ALBUMSFIELDS = 'http://opensocial.myspace.com/roa/09/albums/@supportedFields'
API_OPENSOCIAL_ALBUMS = 'http://opensocial.myspace.com/roa/09/albums/%s/@self/%s'
API_OPENSOCIAL_ADDALBUM = 'http://opensocial.myspace.com/roa/09/albums/%s/@self'

API_OPENSOCIAL_MEDIAITEMSFIELDS = 'http://opensocial.myspace.com/roa/09/mediaItems/@supportedFields'
API_OPENSOCIAL_MEDIAITEMS = 'http://opensocial.myspace.com/roa/09/mediaItems/%s/@self/%s/%s'
API_OPENSOCIAL_ADDPHOTO = 'http://opensocial.myspace.com/roa/09/mediaitems/%s/@self/%s'

API_OPENSOCIAL_MEDIACATITEMS = 'http://opensocial.myspace.com/roa/09/mediaitems/%s/@videos/@supportedcategories/%s'
API_OPENSOCIAL_MEDIAITEMCOMMENTS = 'http://opensocial.myspace.com/roa/09/mediaitemcomments/%s/@self/%s/%s' 

API_OPENSOCIAL_ACTIVITIESFIELDS = 'http://opensocial.myspace.com/roa/09/activities/@supportedFields'
API_OPENSOCIAL_ACTIVITIESVERBS = 'http://opensocial.myspace.com/roa/09/activities/@supportedVerbs'
API_OPENSOCIAL_ACTIVITIESOBJECTTYPES = 'http://opensocial.myspace.com/roa/09/activities/@supportedObjectTypes'
API_OPENSOCIAL_ACTIVITIES = 'http://opensocial.myspace.com/roa/09/activities/%s/@self/%s' 
API_OPENSOCIAL_FRIENDACTIVITIES = 'http://opensocial.myspace.com/roa/09/activities/%s/@friends/%s' 
API_OPENSOCIAL_CREATEACTIVITY = 'http://opensocial.myspace.com/roa/09/activities/%s/@self/@app'

API_OPENSOCIAL_APPDATA = 'http://opensocial.myspace.com/roa/09/appdata/%s/@self/%s'
API_OPENSOCIAL_ADDAPPDATA = 'http://opensocial.myspace.com/roa/09/appdata/%s/@self/%s?fields=%s' 

API_OPENSOCIAL_GROUPSFIELDS = 'http://opensocial.myspace.com/roa/09/groups/@supportedFields'
API_OPENSOCIAL_GROUPS = 'http://opensocial.myspace.com/roa/09/groups/%s'

API_OPENSOCIAL_STATUSMOOD = 'http://opensocial.myspace.com/roa/09/statusmood/%s/@supportedMood'
API_OPENSOCIAL_STATUSMOODID = 'http://opensocial.myspace.com/roa/09/statusmood/%s/@supportedMood/%s'
API_OPENSOCIAL_SELFSTATUS = 'http://opensocial.myspace.com/roa/09/statusmood/%s/@self'
API_OPENSOCIAL_FRIENDSTATUS = 'http://opensocial.myspace.com/roa/09/statusmood/%s/@friends'
API_OPENSOCIAL_SELFHISTORYSTATUS = 'http://opensocial.myspace.com/roa/09/statusmood/%s/@self/history'
API_OPENSOCIAL_FRIENDHISTORYSTATUS = 'http://opensocial.myspace.com/roa/09/statusmood/%s/@friends/history'
API_OPENSOCIAL_STATUSFRIENDID = 'http://opensocial.myspace.com/roa/09/statusmood/%s/@friends/%s'
API_OPENSOCIAL_STATUSHISTORYFRIENDID = 'http://opensocial.myspace.com/roa/09/statusmood/%s/@friends/%s/history'
API_UPDATE_OSTATUS_URL = 'http://opensocial.myspace.com/roa/09/statusmood/%s/@self'
 
API_OPENSOCIAL_STATUSMOODCOMMENTS = 'http://opensocial.myspace.com/roa/09/statusmoodcomments/%s/@self'
API_OPENSOCIAL_POSTSTATUSMOODCOMMENTS = 'http://opensocial.myspace.com/roa/09/statusmoodcomments/%s/@self?statusId=%s'

API_OPENSOCIAL_PEOPLEFIELDS = 'http://opensocial.myspace.com/roa/09/people/@supportedFields' 
API_OPENSOCIAL_PEOPLE = 'http://opensocial.myspace.com/roa/09/people/%s/@self/%s'
API_OPENSOCIAL_PEOPLEFRIENDS = 'http://opensocial.myspace.com/roa/09/people/%s/@friends/%s'

API_OPENSOCIAL_NOTIFICATIONS = 'http://opensocial.myspace.com/roa/09/notifications/%s/@self'  
API_OPENSOCIAL_PROFILECOMMENTS = 'http://opensocial.myspace.com/roa/09/profilecomments/%s/@self' 

class RestV9():
    def __init__(self,objmyspacecontext):
        global context
        context= objmyspacecontext    
    
     
    """  OpenSocial v0.9 - Get Profile Comments        
        Resource:    http://opensocial.myspace.com/roa/09/profilecomments/@me/@self        
        Description: Return all comments available for user profile.
        Parameter:   @person_id (mandatory parameter) current person id e.g: @me
                     @fields (optional parameter). By default, the id of the comment author will be added 
                     to the result set, give the fields=author to get more information on the author
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_ProfileComments        
    """
    def get_profilecomments(self,person_id, fields=None):        
        url = API_OPENSOCIAL_PROFILECOMMENTS % person_id
        return context.callmyspaceapi(url)
        
    
    
    
    """ OpenSocial v0.9 - Retrieve all Album supported Fields        
       Resource:    http://opensocial.myspace.com/roa/09/albums/@supportedFields
       Description: Return all fields available for albums
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Albums
    """    
    def get_albumfields(self):        
        params = {}                 
        oalbumfields_request_url = API_OPENSOCIAL_ALBUMSFIELDS       
        return context.callmyspaceapi(oalbumfields_request_url, parameters=params)



    """ OpenSocial v0.9 - Retrieve Albums       
       Resource:    http://opensocial.myspace.com/roa/09/albums/@me/@self/%s
       Description: Retrieve Albums return all albums available for user, 
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @fields (optional parameter) fields which you want to filter in response                     
                    @startindex (optional parameter)  startIndex must be in the form of startIndex = (count * i) + 1,
                     where i is any non-negative integer, 
                    e.g. if count = 5, startIndex can be 1, 6, 11, 16, etc.
                    @count (optional parameter) total number of records
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Albums    
    """
    def get_albums(self,person_id, fields=None, startindex=None, count=None):            
        
        params = {}
        if fields is not None:
            params['fields'] = fields
        if startindex is not None:
            params['startindex'] = startindex
        if count is not None:
            params['count'] = count
        
        oalbum_request_url = API_OPENSOCIAL_ALBUMS % (person_id , '')
        
        return context.callmyspaceapi(oalbum_request_url, parameters=params)  
      
    
    
    """ OpenSocial v0.9 - Retrieve Album by ID       
       Resource:    http://opensocial.myspace.com/roa/09/albums/@me/@self/%s
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Albums
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @album_id (mandatory parameter)pass the  album id  which you want to get in response.
                    @fields  (optional) return fields which you need in response
       Description: get_albumbyidv9 return a specific album based on passed alumb_id    
    """
    def get_albumbyid(self,person_id, album_id, fields=None):            
        
        params = {}
        if fields is not None:
            params['fields'] = fields            
                   
        oalbum_request_url = API_OPENSOCIAL_ALBUMS % (person_id,album_id)
                 
        return context.callmyspaceapi(oalbum_request_url, parameters=params)
    
    

    """ OpenSocial v0.9 - Add Album       
       Resource:    http://opensocial.myspace.com/roa/09/albums/@me/@self       
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @caption (mandatory parameter)use in place of title. 
                    @location (optional parameter) 
                    @privacy  (optional parameter) specifies visibility for album, 
                    it can be one of 'Everyone', 'FriendsOnly' or 'Me' 
       Description: Creates new album with specified access or with default access of EveryOne (if not
                    specified) 
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Albums
    """   
    def create_album(self,person_id, caption, location=None, privacy='Everyone'):
        
        #validate the privacy param - it can be one of 'Everyone', 'FriendsOnly' or 'Me'
        
        valid_privacy_values = ['Everyone', 'FriendsOnly', 'Me']
        if privacy is not None:
          if privacy not in valid_privacy_values:
                raise MySpaceError('Invalid Parameter Value. list must be one of %s' % str(valid_privacy_values))
                return
        if location is not None:           
            bodytext = '{ "caption": "' + caption + '",  "mediaItemCount":0 ,"msPrivacyLevel" : "' + privacy + '","location" : "' + location + '"}'
            return bodytext
        
        else:
            bodytext = '{ "caption": "' + caption + '",  "mediaItemCount":0 ,"msPrivacyLevel" : "' + privacy + '"}'
                       
        album_create_url = API_OPENSOCIAL_ADDALBUM % person_id        
        params = {}
            
        return context.callmyspaceapi(album_create_url, method='POST', parameters=params, body=bodytext) 
       
       
    """ OpenSocial v0.9 - Update existing Album
       Resource:   http://opensocial.myspace.com/roa/09/albums/@me/@self/%s
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @album_id (mandatory parameter)Id of album which you want to update
                    @caption (Optional parameter)use in place of title. 
                    @location (optional parameter) 
                    @privacy  (optional parameter) specifies visibility for album, 
                    it can be one of 'Everyone', 'FriendsOnly' or 'Me' 
       Description: Update album with new values of parameters specified 
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Albums            
    """
    def update_album(self,person_id, album_id, caption=None, location=None, privacy='Everyone'):
        
        #validate the privacy param - it can be one of 'Everyone', 'FriendsOnly' or 'Me'
        
        valid_privacy_values = ['Everyone', 'FriendsOnly', 'Me']
        if privacy is not None:
          if privacy not in valid_privacy_values:
                raise MySpaceError('Invalid Parameter Value. list must be one of %s' % str(valid_privacy_values))
                return
                   
        bodytext = '{ "caption": "' + caption + '", "id" :"' + str(album_id) + '", "mediaItemCount":0 ,"msPrivacyLevel" : "' + privacy + '"}'
                       
        album_create_url = API_OPENSOCIAL_ALBUMS % (person_id,album_id)         
        params = {}
            
        return context.callmyspaceapi(album_create_url, method='PUT', parameters=params, body=bodytext)
    
    
    """ OpenSocial v0.9 - Retrieve all media item supported Fields 
       Resource:    http://opensocial.myspace.com/roa/09/mediaItems/@supportedFields      
       Description: Update album for with new values of parameters specified 
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """           
    def get_mediaitemfields(self):
        omediaitemfields_request_url = API_OPENSOCIAL_MEDIAITEMSFIELDS        
        return context.callmyspaceapi(omediaitemfields_request_url)   
    
 
    """ OpenSocial v0.9 - Get Media Items
       Resource:    http://opensocial.myspace.com/roa/09/mediaItems/{personId}/{selector}/{albumId}/{mediaItemId}
       Description: Retrieve items from an Album based on album_id
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @album_id (mandatory parameter)Id of album for which you want to get data
                    @startindex (optional parameter)  startIndex must be in the form of startIndex = (count * i) + 1,
                    where i is any non-negative integer, 
                    e.g. if count = 5, startIndex can be 1, 6, 11, 16, etc.
                    @count (optional parameter) total number of records        
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """              
    def get_mediaitems(self,person_id, album_id, startindex=None, count=None):        
        context.validate_params(locals())           
        
        params = {}
        if startindex is not None:
            params['startindex'] = startindex
        if count is not None:
            params['count'] = count
            
        omedia_request_url = API_OPENSOCIAL_MEDIAITEMS % (person_id,album_id , '')  
               
        return context.callmyspaceapi(omedia_request_url)
    
    
    
    """ OpenSocial v0.9 - Get Media Items by ID
       Resource:    http://opensocial.myspace.com/roa/09/mediaItems/{personId}/{selector}/{albumId}/{mediaItemId}
       Description: Retrieve a single MediaItem from an Album based on album_id and media_id
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @album_id (mandatory parameter)Id of album for which you want to get data
                    @media_id (mandatory parameter)Id of media items for which you want to get data
                    @startindex (optional parameter)  startIndex must be in the form of startIndex = (count * i) + 1,
                    where i is any non-negative integer, 
                    e.g. if count = 5, startIndex can be 1, 6, 11, 16, etc.
                    @count (optional parameter) total number of records        
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """     
    def get_mediaitemsbymediaid(self, person_id,album_id, media_id):        
        context.validate_params(locals())
        omedia_request_url = API_OPENSOCIAL_MEDIAITEMS % (person_id,album_id, media_id) 
                       
        return context.callmyspaceapi(omedia_request_url)
    
    """ OpenSocial v0.9 - Get Media Items by Category
       Resource:    #http://opensocial.myspace.com/roa/09/mediaitems/{personId}/@videos/@supportedcategories
       Description: Retrieve MediaItem(Video) from suuported cat
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me                            
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """     
    def get_videocatergories(self, person_id, startindex=None, count=None):        
        context.validate_params(locals())
        params = {}
        if startindex is not None:
            params['startindex'] = startindex
        if count is not None:
            params['count'] = count
        omedia_request_url = API_OPENSOCIAL_MEDIACATITEMS % (person_id,'')                       
        return context.callmyspaceapi(omedia_request_url,parameters=params)
    
    """ OpenSocial v0.9 - Get Media Items by Category ID
       Resource:    #http://opensocial.myspace.com/roa/09/mediaitems/{personId}/@videos/@supportedcategories/{categoryId}
       Description: Retrieve MediaItem(Video) from suuported cat
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me                            
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """     
    def get_videocatergoriesbyid(self, person_id,cat_id):        
        context.validate_params(locals())
        omedia_request_url = API_OPENSOCIAL_MEDIACATITEMS % (person_id,cat_id)                       
        return context.callmyspaceapi(omedia_request_url)
    
    
    
    """ OpenSocial v0.9 - Add Photo
        How to use this Method
        Make sure you have image file (Say TEST.JPG) available in same folder where your source resides
        fin = open(r'TEST.jpg','rb')
        data = fin.read()
        photo_added = ms.add_photoalbum(person_id="@me",caption="My test Photo",album_id='myspace.com.album.1433449',data=data)
        fin.close()
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """          
    def add_photoalbum(self,person_id,caption,album_id,data):  
                 
        #album_create_url = 'http://opensocial.myspace.com/roa/09/mediaitems/@me/@self/myspace.com.album.1433449'
        album_create_url = API_OPENSOCIAL_ADDPHOTO % (person_id,album_id)
        params = {}
        
        params["type"]= "IMAGE"
        params["caption"] = caption
                    
        bodytext=data
        return context.callmyspaceapi(album_create_url, method='POST', parameters=params, body=bodytext,flag='image') 
       
       
    """ OpenSocial v0.9 - Add Video
        How to use this Method
        Make sure you have video file (Say TEST.wmv) available in same folder where your source resides
         #fin = open(r'test.wmv','rb')
         # fin = open(r'TEST.wmv','rb')
         # data = fin.read()               
        #albums_data1 = ms.add_videotoalbum(person_id="@me",album_id='0',caption='My Video',description='Video Description',tags = 'Video tags', language='en-us',data=data,mscategories=14)
        #fin.close()
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """   
    def add_video(self,person_id,album_id,caption,description,tags,language,data,mscategories):       
  
        
        album_create_url = API_OPENSOCIAL_ADDPHOTO % (person_id,album_id)
        params = {}             
        params["type"]= "VIDEO"
        params["caption"] = caption
        params["description"] = description
        params["tags"] = tags
        params["msCategories"]= mscategories
        params["language"] = language
         
        bodytext=data
        return context.callmyspaceapi(album_create_url, method='POST', parameters=params, body=bodytext,flag='video') 
  


    """ OpenSocial v0.9 MediaItemComments
       Resource:    http://opensocial.myspace.com/roa/09/mediaitemcomments/{personId}/@self/{albumId}/{mediaItemId}
       Description: Get comments associated with media item, based on album_id and media_id
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @album_id (mandatory parameter)Id of album which you want to update
                    @media_id (mandatory parameter)Id of media items for which you want to get data                    
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_MediaItemComments           
    """          
    def get_mediaitemscomments(self,person_id, album_id, media_id):                         
        omediacomments_request_url = API_OPENSOCIAL_MEDIAITEMCOMMENTS % (person_id,album_id , media_id)
        return context.callmyspaceapi(omediacomments_request_url) 
    
    
    """ OpenSocial v0.9 - Retrieve all activity supported Fields 
       Resource:    http://opensocial.myspace.com/roa/09/activities/@supportedFields    
       Description: Retrieve all activity supported fields
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """   
    def get_activitiesfields(self):
        oactivitiesmfields_request_url = API_OPENSOCIAL_ACTIVITIESFIELDS        
        return context.callmyspaceapi(oactivitiesmfields_request_url) 
         
   
    """ OpenSocial v0.9 - Retrieve all supported verbs 
       Resource:    http://opensocial.myspace.com/roa/09/activities/@supportedVerbs       
       Description: Retrieve all activity supported verbs
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """   
    def get_activitiesverbs(self):
        oactivitiesmverbs_request_url = API_OPENSOCIAL_ACTIVITIESVERBS        
        return context.callmyspaceapi(oactivitiesmverbs_request_url)  
    
    
    """ OpenSocial v0.9 - Retrieve all supported Object Types 
       Resource:    http://opensocial.myspace.com/roa/09/activities/@supportedObjectTypes      
       Description: Retrieve all activity supported Object Types
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """   
    def get_activitiesobjecttypes(self):
        oactivitiesobjecttypes_request_url = API_OPENSOCIAL_ACTIVITIESOBJECTTYPES       
        return context.callmyspaceapi(oactivitiesobjecttypes_request_url)     
     
    
    
    """ OpenSocial v0.9 -Retrieve viewer activities     
        Resource:    http://opensocial.myspace.com/roa/09/activities/{personId}/{selector}       
        Description: Return all activities available for viewer
        Parameter:   @person_id (mandatory parameter) current person id e.g: @me
                     @fields (optional parameter).------------------------------
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Activities        
    """
    def get_activities(self,person_id, fields=None):
          
        params = {}
        if fields is not None:
            params['fields'] = fields           
        
        oactivities_request_url = API_OPENSOCIAL_ACTIVITIES % (person_id,'')           
        return context.callmyspaceapi(oactivities_request_url, parameters=params)
    
    
    """ OpenSocial v0.9 - Retrieve viewer activities by appID 
        Resource:    http://opensocial.myspace.com/roa/09/activities/{personId}/{selector}       
        Description: Return all activities available for viewer for an appID specified in parameter
        Parameter:   @app_id (mandatory parameter) refers to applicaiton id for which user wants to check activities
                     @fields (optional parameter).------------------------------                     
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Activities        
    """
    def get_activitiesbyappid(self,person_id, app_id, fields=None):
        
        params = {}
        if fields is not None:
            params['fields'] = fields
            
        oactivities_request_url = API_OPENSOCIAL_ACTIVITIES % (person_id,app_id)      
        
        return context.callmyspaceapi(oactivities_request_url, parameters=params)
    
    

    """ OpenSocial v0.9 - Retrieve friend activities.
        Resource:    http://opensocial.myspace.com/roa/09/activities/{personId}/{selector}       
        Description: Return all activities available for friend.
        Parameter:   @person_id (mandatory parameter) current person id e.g: @me
                     @fields (optional parameter).specific fields
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Activities        
    """
    def get_friendactivities(self,person_id, fields=None):
            
        params = {}
        if fields is not None:
            params['fields'] = fields           
        
        oactivities_request_url = API_OPENSOCIAL_FRIENDACTIVITIES % (person_id,'')
           
        return context.callmyspaceapi(oactivities_request_url, parameters=params)
    
    
    """ OpenSocial v0.9 - Retrieve friend activities by appID 
        Resource:    http://opensocial.myspace.com/roa/09/activities/{personId}/{selector}       
        Description: Return all activities available for friend for an appID specified in parameter
        Parameter:   @person_id (mandatory parameter) current person id e.g: @me
                     @app_id (mandatory parameter) refers to applicaiton id for which user wants to check activities    
                     @fields (optional parameter).specific fields
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Activities        
    """
    def get_friendactivitiesbyappid(self, person_id, app_id, fields=None):
          
        params = {}
        if fields is not None:
            params['fields'] = fields
            
        oactivities_request_url = API_OPENSOCIAL_FRIENDACTIVITIES % (person_id,app_id)
        return context.callmyspaceapi(oactivities_request_url, parameters=params)
    
    
         
    def create_activity(self,person_id,external_id,title,body,templateparams, title_id):
                
        bodytext= '{"externalId":"'+external_id+'","id":"+myspace.com.activity.-1","title":"'+title+'","body":"'+body+'","templateParams":'+templateparams+',"titleId":"'+title_id+'"}'
        
        activity_create_url = API_OPENSOCIAL_CREATEACTIVITY % person_id                
        params = {}                    
        return context.callmyspaceapi(activity_create_url, method='POST', parameters=params, body=bodytext) 
           
           

    """ OpenSocial v0.9 - Retrieve all/Single key in AppData for a single user 
        Resource:    http://opensocial.myspace.com/roa/09/appdata/{personId}/{selector}/{appId}       
        Description: Retrieve all AppData for a single user 
        Parameter:   @person_id (mandatory parameter) current person id e.g: @me
                     @app_id (mandatory parameter) refers to applicaiton id for which user wants to get data    
                     @fields (optional parameter).The fields correspond to keys in the AppData. One uses fields
                      to only retrieve specific keys. If the request omits fields, all AppData per user will be returned.
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_AppData       
    """    
    def get_appdata(self, person_id,app_id , fields=None):
        context.validate_params(locals())
        appdata_request_url = API_OPENSOCIAL_APPDATA % (person_id,app_id)
        
        params = {}
        if fields is not None:
            params['fields'] = fields
            
        return context.callmyspaceapi(appdata_request_url, parameters=params)
    
    
    
    """ OpenSocial v0.9 - Add a single key to AppData for a single user
        Resource:    http://opensocial.myspace.com/roa/09/appData/@me/@self/       
        Description: Add a single key AppData for a single user 
        Parameter:   @person_id (mandatory parameter) current person id e.g: @me
                     @app_id (mandatory parameter) refers to applicaiton id for which user wants to enter data    
                     @key (mandatory parameter).refers to the name of key which will be entered
                     @value (mandatory parameter).refers to the value of key which will be stored
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_AppData       
    """
    def add_appdata(self, person_id, app_id, key, value):
           
        bodytext = '{"userId":"' + str(person_id) + '", "appData":[{"key":"' + key + '","value":"' + value + '"}]}'        
        appdata_request_url = API_OPENSOCIAL_ADDAPPDATA % (person_id,app_id, key)
       
        params = {}
        
        return context.callmyspaceapi(appdata_request_url, method='POST', parameters=params, body=bodytext) 



    """ OpenSocial v0.9 - Update a single key to AppData for a single user
        Resource:    http://opensocial.myspace.com/roa/09/appData/@me/@self/       
        Description: Add a single key AppData for a single user 
        Parameter:   @person_id (mandatory parameter) current person id e.g: @me
                     @app_id (mandatory parameter) refers to applicaiton id for which user wants to update data    
                     @key (mandatory parameter).refers to the name of key which will be updated
                     @value (mandatory parameter).refers to the value of key which will be updated
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_AppData       
    """
    def update_appdata(self, person_id, app_id, key, value):
           
        bodytext = '{"userId":"' + str(person_id) + '", "appData":[{"key":"' + key + '","value":"' + value + '"}]}'        
        appdata_request_url = API_OPENSOCIAL_ADDAPPDATA % (person_id,app_id, key)
       
        params = {}
            
        return context.callmyspaceapi(appdata_request_url, method='PUT', parameters=params, body=bodytext)
     
     
     
    """ OpenSocial v0.9 - Delete single key to AppData for a single user 
        Resource:    http://opensocial.myspace.com/roa/09/appData/@me/@self/       
        Description: Delete a single key AppData for a single user 
        Parameter:   @person_id (mandatory parameter) current person id e.g: @me
                     @app_id (mandatory parameter) refers to applicaiton id for which user wants to delete data    
                     @fields (mandatory parameter).refers to the name of key which will be updated
                     @value (mandatory parameter).refers to the value of key which will be updated
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_AppData
        ------------------------       
    """
    def delete_appdata(self, person_id,app_id, fields):
                                  
        #bodytext = '{"userId":329772253, "appData":[{"key":"' + key+'","value":"'+value+'"}]}'
        appdata_request_url = API_OPENSOCIAL_ADDAPPDATA % (person_id,app_id)            
        params = {} 
        #params["fields"] = fields
            
        return context.callmyspaceapi(appdata_request_url, method='DELETE', parameters=params) 
              
     
    """ OpenSocial v0.9 Groups- Retrieve all supported fields   
       Resource:    http://opensocial.myspace.com/roa/09/groups/@supportedFields       
       Description: Retrieve all group supported fields
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Groups           
    """         
    def get_groupfields(self):
        ogroupsfields_request_url = API_OPENSOCIAL_GROUPSFIELDS        
        return context.callmyspaceapi(ogroupsfields_request_url)   
    

    """ OpenSocial v0.9 - Retrieve all groups for current user   
       Resource:    http://opensocial.myspace.com/roa/09/groups/@me       
       Description: Retrieve all groups for current user fields
       Parameter:   @person_id (mandatory parameter) current person id e.g: @me
                    @startindex (optional parameter)  startIndex must be in the form of startIndex = (count * i) + 1,
                    where i is any non-negative integer, 
                    e.g. if count = 5, startIndex can be 1, 6, 11, 16, etc.
                    @count (optional parameter) total number of records
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Groups           
    """       
    def get_groups(self,person_id, startindex=None, count=None):
        
        params = {}
        if startindex is not None:
            params['startindex'] = startindex
        if count is not None:
            params['count'] = count
            
        ogroups_request_url = API_OPENSOCIAL_GROUPS % person_id  
        return context.callmyspaceapi(ogroups_request_url, parameters=params) 
    

    """ OpenSocial v0.9 People- Retrieve all supported fields   
       Resource:    http://opensocial.myspace.com/roa/09/people/@supportedFields        
       Description: Retrieve all people supported fields
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_People           
    """ 
    def get_peoplefields(self):
        opeoplefields_request_url = API_OPENSOCIAL_PEOPLEFIELDS     
        return context.callmyspaceapi(opeoplefields_request_url)     
    
    
    
    """ OpenSocial v0.9 People- Retrieve viewer data   
       Resource:    http://opensocial.myspace.com/roa/09/people/@me/@self        
       Description: Retrieve all viewer data
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @fields     (optional parameter) specific fields
                    @filterby   (optional parameter) some valid values : {topFriends | toponlineFriends | hasApp etc }                 
                    @filterop   (optional parameter) some valid values : {contains | equals etc }
                    @filtervalue(optional parameter) some valid values : {true | false | specific value etc }
                    @format     (optional parameter)  Determines the format of the response. We currently support json and xml
                    @startindex (optional parameter)  startIndex must be in the form of startIndex = (count * i) + 1,
                    where i is any non-negative integer, 
                    e.g. if count = 5, startIndex can be 1, 6, 11, 16, etc.
                    @count (optional parameter) total number of records                
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_People           
    """     
    def get_person(self,person_id, fields=None, filterby=None, filterop=None, filtervalue=None,
                     format=None, startindex=None, count=None):
        
        params = {}
        
        if fields is not None:
            params['fields'] = fields
        if filterby is not None:
            params['filterby'] = filterby
        if filterop is not None:
            params['filterop'] = filterop
        if filtervalue is not None:
            params['filtervalue'] = filtervalue
        if format is not None:
            params['format'] = format
        if startindex is not None:
            params['startindex'] = startindex
        if count is not None:
            params['count'] = count
            
        opeople_request_url = API_OPENSOCIAL_PEOPLE % (person_id,'')
        return context.callmyspaceapi(opeople_request_url, parameters=params) 
    
    
    
    
    """ OpenSocial v0.9 People- Retrieve viewer data   
       Resource:    http://opensocial.myspace.com/roa/09/people/{personId}/{selector}/{friendId}       
       Description: Retrieve all viewer data
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @fields     (optional parameter)
                    @filterby   (optional parameter) some valid values : {topFriends | toponlineFriends | hasApp etc }                 
                    @filterop   (optional parameter) some valid values : {contains | equals etc }
                    @filtervalue(optional parameter) some valid values : {true | false | specific value etc }
                    @format     (optional parameter) Determines the format of the response. We currently support json and xml
                    @startindex (optional parameter)  startIndex must be in the form of startIndex = (count * i) + 1,
                    where i is any non-negative integer, 
                    e.g. if count = 5, startIndex can be 1, 6, 11, 16, etc.
                    @count (optional parameter) total number of records                
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_People           
    """       
    def get_friends(self, person_id, fields=None, filterby=None, filterop=None, filtervalue=None,
                     format=None, startindex=None, count=None):
        
        params = {}
        
        if fields is not None:
            params['fields'] = fields
        if filterby is not None:
            params['filterby'] = filterby
        if filterop is not None:
            params['filterop'] = filterop
        if filtervalue is not None:
            params['filtervalue'] = filtervalue
        if format is not None:
            params['format'] = format
        if startindex is not None:
            params['startindex'] = startindex
        if count is not None:
            params['count'] = count
            
        opeople_request_url = API_OPENSOCIAL_PEOPLEFRIENDS % (person_id,'')
        return context.callmyspaceapi(opeople_request_url, parameters=params) 
    
    
    
    """ OpenSocial v0.9 People- Retrieve viewer data   
       Resource:    http://opensocial.myspace.com/roa/09/people/{personId}/{selector}/{friendId}       
       Description: Retrieve all viewer data
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @fields     (optional parameter) specific fields
                    @filterby   (optional parameter) some valid values : {topFriends | toponlineFriends | hasApp etc }                 
                    @filterop   (optional parameter) some valid values : {contains | equals etc }
                    @filtervalue(optional parameter) some valid values : {true | false | specific value etc }
                    @format     (optional parameter) Determines the format of the response. We currently support json and xml
                    @startindex (optional parameter)  startIndex must be in the form of startIndex = (count * i) + 1,
                    where i is any non-negative integer, 
                    e.g. if count = 5, startIndex can be 1, 6, 11, 16, etc.
                    @count (optional parameter) total number of records                
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_People           
    """   
    def get_peoplebyfriendid(self,person_id, friend_id, fields=None):
        
        params = {}
        
        if fields is not None:
            params['fields'] = fields       
        
        opeople_request_url = API_OPENSOCIAL_PEOPLEFRIENDS % (person_id,friend_id)
        
        return context.callmyspaceapi(opeople_request_url, parameters=params) 
    
    
    
    """OpenSocial v0.9 StatusMood - Retrieve all supported moods    
       Resource:    http://opensocial.myspace.com/roa/09/statusmood/@me/@supportedMood      
       Description: Retrieve all supported moods 
       Parameters:  person_id (mandatory parameter) current person id e.g: @me                       
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood          
    """   
    def get_supportedsmoods(self,person_id):     
        ostatus_request_url = API_OPENSOCIAL_STATUSMOOD % person_id           
        return context.callmyspaceapi(ostatus_request_url)
    
    
    """OpenSocial v0.9 StatusMood - Retrieve all supported moods by id 
       Resource:    http://opensocial.myspace.com/roa/09/statusmood/{personId}/@supportedMood/{moodId}      
       Description: Retrieve all supported moods by id  
       Parameters:  person_id (mandatory parameter) current person id e.g: @me       
                    mood_id (Optional parameter) id of mood which you want to retrive                
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood          
    """   
    def get_supportedsmoodbyid(self,person_id, mood_id=None):
        
        ostatus_request_url = API_OPENSOCIAL_STATUSMOODID % (person_id,mood_id)    
        return context.callmyspaceapi(ostatus_request_url)
    
    
    """ OpenSocial v0.9 Retrieve a status & mood for user
        Resource:    http://opensocial.myspace.com/roa/09/statusmood/{personId}/{selector}
        Description: Retrieve a status & mood for user
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me 
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood
    """
    def get_statusmood(self,person_id):  
        ostatus_request_url = API_OPENSOCIAL_SELFSTATUS  % person_id         
        return context.callmyspaceapi(ostatus_request_url)

  
       
    """ OpenSocial v0.9 Retrieve a status & mood for friend
        Resource:    http://opensocial.myspace.com/roa/09/statusmood/{personId}/{selector}
        Description: Retrieve a status & mood for user
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me 
                     @filterby (optional parameter) some valid values : {topFriends | toponlineFriends | hasApp etc }
                     @filterop (optional parameter) some valid values : {contains | equals etc }
                     @filtervalue (optional parameter)  some valid values : {true | false | specific value etc }
                     @includeself (optional parameter) current user should included or not
                     @culture (optional parameter) culture for which you wan to select value
                     @fields (optional parameter) specific fields
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood
    """
    def get_friendstatusmood(self, person_id, filterby=None, filterop=None, filtervalue=None, includeself=None,
                              culture=None, fields=None):         
        params = {}
        if filterby is not None:
            params['filterby'] = filterby
        if filterop is not None:
            params['filterop'] = filterop
        if filtervalue is not None:
            params['filtervalue'] = filtervalue
        if includeself is not None:
            params['includeself'] = includeself
        if culture is not None:
            params['culture'] = culture
        if fields is not None:
            params['fields'] = fields    
                   
        ostatus_request_url = API_OPENSOCIAL_FRIENDSTATUS % person_id           
        return context.callmyspaceapi(ostatus_request_url, parameters=params)
    
   
    """ OpenSocial v0.9 Retrieve a status & mood history for user
        Resource:    http://opensocial.myspace.com/roa/09/statusmood/{personId}/{selector}/history 
        Description: Retrieve a status & mood history for user
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me 
                     @fields (optional parameter) specific fields
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood
    """
    def get_selfstatusmoodhistory(self,person_id, fields=None):
        #context.validate_params(locals()) not needed here     
        params = {}
        if fields is not None:
            params['fields'] = fields            
       
        ostatus_request_url = API_OPENSOCIAL_SELFHISTORYSTATUS % person_id       
        return context.callmyspaceapi(ostatus_request_url, parameters=params)
   
   

    """ OpenSocial v0.9 Retrieve a status & mood history for friends
        Resource:    http://opensocial.myspace.com/roa/09/statusmood/{personId}/{selector}/history 
        Description: Retrieve a status & mood history for friends
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me 
                     @filterby (optional parameter) some valid values : {topFriends | toponlineFriends | hasApp etc }
                     @filterop (optional parameter) some valid values : {contains | equals etc }
                     @filtervalue (optional parameter)  some valid values : {true | false | specific value etc }
                     @includeself (optional parameter) current user should included or not
                     @culture (optional parameter) culture for which you wan to select value
                     @fields (optional parameter) specific fields
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood
    """
    def get_friendstatusmoodhistory(self,person_id, filterby=None, filterop=None, filtervalue=None, includeself=None,
                              culture=None, fields=None, startIndex=None, itemsPerPage=None):          
        
        params = {}
        if filterby is not None:
            params['filterby'] = filterby
        if filterop is not None:
            params['filterop'] = filterop
        if filtervalue is not None:
            params['filtervalue'] = filtervalue
        if includeself is not None:
            params['includeself'] = includeself
        if culture is not None:
            params['culture'] = culture
        if fields is not None:
            params['fields'] = fields    
        if startIndex is not None:
            params['startIndex'] = startIndex    
        if itemsPerPage is not None:
            params['itemsPerPage'] = itemsPerPage    
        
                   
        ostatus_request_url = API_OPENSOCIAL_FRIENDHISTORYSTATUS  % person_id         
        return context.callmyspaceapi(ostatus_request_url, parameters=params)


    """ OpenSocial v0.9 Retrieve a status & mood history for a particular friend
        Resource:    http://opensocial.myspace.com/roa/09/statusmood/{personId}/{selector}/history 
        Description: Retrieve a status & mood for a friend
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me 
                     @friend_id (mandatory parameter) id of friend for which you want to retreive data
                     @filterby (optional parameter) some valid values : {topFriends | toponlineFriends | hasApp etc }
                     @filterop (optional parameter) some valid values : {contains | equals etc }
                     @filtervalue (optional parameter)  some valid values : {true | false | specific value etc }
                     @includeself (optional parameter) current user should included or not
                     @culture (optional parameter) culture for which you wan to select value
                     @fields (optional parameter) specific fields
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood
    """
    def get_statusmoodbyfriendid(self,person_id, friend_id, filterby=None, filterop=None, filtervalue=None, includeself=None,
                              culture=None, fields=None, startIndex=None, itemsPerPage=None):          
        
        params = {}
        if filterby is not None:
            params['filterby'] = filterby
        if filterop is not None:
            params['filterop'] = filterop
        if filtervalue is not None:
            params['filtervalue'] = filtervalue
        if includeself is not None:
            params['includeself'] = includeself
        if culture is not None:
            params['culture'] = culture
        if fields is not None:
            params['fields'] = fields    
        if startIndex is not None:
            params['startIndex'] = startIndex    
        if itemsPerPage is not None:
            params['itemsPerPage'] = itemsPerPage    
        
                   
        ostatus_request_url = API_OPENSOCIAL_STATUSFRIENDID % (person_id,friend_id)               
        return context.callmyspaceapi(ostatus_request_url, parameters=params)     
    
    
    
    """ OpenSocial v0.9 Retrieve a status & mood history for a particular friend
        Resource:    http://opensocial.myspace.com/roa/09/statusmood/{personId}/{selector}/history 
        Description: Retrieve a status & mood for a friend
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                     @friend_id (mandatory parameter) id of friend for which you want to retreive data 
                     @filterby (optional parameter) some valid values : {topFriends | toponlineFriends | hasApp etc }
                     @filterop (optional parameter) some valid values : {contains | equals etc }
                     @filtervalue (optional parameter)  some valid values : {true | false | specific value etc }
                     @includeself (optional parameter) current user should included or not
                     @culture (optional parameter) culture for which you wan to select value
                     @fields (optional parameter) specific fields
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood
    """
    def get_statusmoodhistorybyfriendid(self,person_id, friend_id, filterby=None, filterop=None, filtervalue=None, includeself=None,
                              culture=None, fields=None, startIndex=None, itemsPerPage=None):          
        
        params = {}
        if filterby is not None:
            params['filterby'] = filterby
        if filterop is not None:
            params['filterop'] = filterop
        if filtervalue is not None:
            params['filtervalue'] = filtervalue
        if includeself is not None:
            params['includeself'] = includeself
        if culture is not None:
            params['culture'] = culture
        if fields is not None:
            params['fields'] = fields    
        if startIndex is not None:
            params['startIndex'] = startIndex    
        if itemsPerPage is not None:
            params['itemsPerPage'] = itemsPerPage    
        
                   
        ostatus_request_url = API_OPENSOCIAL_STATUSHISTORYFRIENDID % (person_id,friend_id )        
          
        return context.callmyspaceapi(ostatus_request_url, parameters=params)     
     
     
    """ OpenSocial v0.9 Update Status Mood
        Resource:    http://opensocial.myspace.com/roa/09/statusmood/@me/@self 
        Description: Update/Set Status Mood
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    Possible values for option parameters
                    {
                    "currentLocation":{
                        "latitude":"47.604832",
                        "longitude":"-122.337549"
                    },
                    "moodName":"excited",
                    "status":"Working on Python SDK"
                    }    
                    Example : 
                    set_statusv9(person_id="@me",latitude='47',longitude='122',moodname='excited',status='Pythond SDK Completed')                
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood
    """     
    def set_status(self,person_id, latitude=None, longitude=None, moodname=None, status=None):

        params = {}
        
       
        bodyparam = '{"currentLocation":{"latitude":"' + str(latitude) + '","longitude":"' + str(longitude) + '"},"moodName":"' + str(moodname) + '","status":"' + str(status) + '"}'        
        update_ostatus_url = API_UPDATE_OSTATUS_URL % person_id
        # setting get_raw_status=True since the REST API does not return any data on success
        return context.callmyspaceapi(update_ostatus_url, method='PUT', parameters=params, body=bodyparam, get_raw_response=True)


   
    """ OpenSocial v0.9 Get StatusMoodComments
        Resource:    http://opensocial.myspace.com/roa/09/statusmoodcomments/{personId}/@self  
        Description: Get all Status mood comments
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me                                    
        Details:    http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMoodComments
    """     
    def get_statusmoodcomments(self,person_id,status_id):              
        params = {}
        params["statusId"]=status_id
        ostatuscomments_request_url = API_OPENSOCIAL_STATUSMOODCOMMENTS % person_id
        
        return context.callmyspaceapi(ostatuscomments_request_url,parameters=params)
    
  
    """ OpenSocial v0.9 Set StatusMoodComments
        Resource:    #http://opensocial.myspace.com/roa/09/statusmoodcomments/{personId}/@self?statusId={statusId} 
        Description: Set Status mood comments for a particular s
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                     @body (mandatory parameter) body of status comment
                     @statusid(mandatory paramter) id of parameter for which comment is posted                                    
        Details:    http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMoodComments
    """   
    def set_statusmoodcomments(self,person_id, body, status_id):
    #def set_statusv9(self):
 
        params = {}
        params["statusId"] = status_id
        bodyparam = '{"body":"'+body+'"}'        
        
        ostatuscomments_request_url = API_OPENSOCIAL_STATUSMOODCOMMENTS % person_id                
        return context.callmyspaceapi(ostatuscomments_request_url, method='POST', parameters=params, body=bodyparam,flag='true')

 
    """OpenSocial v0.9 Notifications
        send_notification Usage:
        
        ms = MySpace(ckeynsecret.CONSUMER_KEY, ckeynsecret.CONSUMER_SECRET)
      templateparam ='[{"key":"content","value":"Test notification content from python sdk"},\
                                {"key":"button0_surface","value":"canvas"},\
                                {"key":"button0_label","value":"Go To App Canvas"},\
                                {"key":"button1_label","value":"Go To App Profile"}]'
      notifcation_data = ms.send_notification(person_id="333220680", recipientids="333220680", templateparams=templateparam, mediaitems='http://opensocial.myspace.com/roa/09/mediaitemcomments/333220680/@self')
    """    
    def send_notification(self,person_id, recipientids, templateparams, mediaitems):
                        
        params = {}       
       
        strbody ='{"mediaItems":[{"msMediaItemUri":"'+mediaitems+'"}],"recipientIds":["'+recipientids+'"], "templateParameters": '+templateparams+'}'       
        send_onotification_url = API_OPENSOCIAL_NOTIFICATIONS % person_id        
        return context.callmyspaceapi(send_onotification_url, method='POST', body=strbody, parameters=params)
    
 