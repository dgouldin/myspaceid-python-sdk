#!/usr/bin/python
#
# Copyright (C) 2007, 2008 MySpace Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = 'cnanga@myspace.com (Chak Nanga)'

from oauthlib import oauth
from context.MySpaceContext import MySpaceContext
from Api.PortableContact import PortableContact
from Api.OpenSearch import OpenSearch
from Api.RestV1 import RestV1
from Api.RestV9 import RestV9
from Api.RealStream import RealStream  
 
__all__ = [
    'MySpace',
    ]

API_USERINFO_URL = 'http://api.myspace.com/v1/user.json'

    
class MySpace():

    
    """Constructor can be invoked with or without the oauth token key/secret.
    
       Invoke it without the token for:
          - the oauth request_token and access_token API calls
          - "onsite" application calls i.e. for opensocial apps that are hosted in an iframe
          
       Invoke it with the token for:
          - MySpace ID application calls
    """
 #   global objmyspacecontext
    
    def __init__(self, consumer_key, consumer_secret, oauth_token_key=None, oauth_token_secret=None):
      global objmyspacecontext 
      objmyspacecontext = MySpaceContext(consumer_key, consumer_secret, oauth_token_key, oauth_token_secret)
      
      global search 
      search = OpenSearch(objmyspacecontext)
      
      global roaobj
      roaobj = RestV9(objmyspacecontext)
      
      global realtimeobj
      realtimeobj = RealStream(objmyspacecontext)
      
      global pocoobj
      pocoobj = PortableContact(objmyspacecontext)
      
      global restv1obj
      restv1obj = RestV1(objmyspacecontext)

          
    def get_access_token( self,request_token):      
        resp=objmyspacecontext.get_access_token(request_token)        
        return resp
    
    
    def get_request_token(self):              
        resp =  objmyspacecontext.get_request_token()
        return resp
 
 
    def get_authorization_url(self, token, callback_url):        
        return objmyspacecontext.get_authorization_url(token,callback_url)

 
 
    """MySpace REST API wrapper functions 
    """  
    def get_userid(self):
               
        user_info = objmyspacecontext.callmyspaceapi(API_USERINFO_URL)        
        return user_info['userId']
    
    
    """  Open Search
     Resource: http://api.myspace.com/opensearch/people?
     Details:  http://wiki.developer.myspace.com/index.php?title=Open_Search
     Description: Get People Search
     @param mixed   $searchTerms   (mandatory parameter)search keywords
     @param integer $startIndex    Indicates the index of the first item to retrieve from the query set
     @param integer $count            total number of records
     @param string  $searchBy      which field the search should go through. Default is all the fields (yomi is only available to ja-jp culture) [ex. searchBy=name or searchBy=displayname or searchBy=email or searchBy=yomi] 
     @param string  $gender        the gender to filter on; default is no preference or both [ex. gender=m or gender=f] 
     @param bool    $hasPhoto      filter for those who only has photo; default is either [ex. hasPhoto=on] 
     @param integer $minAge        minimum age to start the search (same filter as site search) [ex. minAge=18] 
     @param integer $maxAge        maximum age to end the search with (same filter as site search) [ex. maxAge=68] 
     @param string  $location      the location field such as city state and country to search for [ex. location=US] 
     @param integer $distance      distance away from location to return results; default is miles; depending on culture passed in it can be kilometers [ex. distance=25] 
     @param mixed   $latitude         geo latitude to search; combination with longitude required when used [ex. latitude=1] (does not work with location field) 
     @param mixed   $longitude     geo longtitude to search; combination with latitude is required when used [ex. longitude=1] (does not work with location field) 
     @param string  $culture         the culture context of the search; for instance japan is ja-jp; default is en-us [ex. culture=en-us] 
     @param string  $countryCode   countryCode to search with [ex. countryCode=CA] (this is similar to culture=en-CA) 
     @return object of python object representing the JSON in which the list of search
    """  
    def search_people(self, searchTerms, format=None, count=None,
                   startPage=None, searchBy=None, gender=None,
                   hasPhoto=None, minAge=None, maxAge=None,
                   location=None , distance=None, latitude=None,
                   culture=None, countryCode=None):
        
        return search.search_people (searchTerms, format, count,
                   startPage, searchBy, gender,
                   hasPhoto, minAge, maxAge,
                   location , distance, latitude,
                   culture, countryCode)
        
    """ Open Search
     Resource: http://api.myspace.com/opensearch/images?
     Details:  http://wiki.developer.myspace.com/index.php?title=Open_Search
     Description: Get Image Search
     @param mixed   $searchTerms   (mandatory parameter)search keywords
     @param integer $startIndex    Indicates the index of the first item to retrieve from the query set
     @param integer $count            total number of records
     @param string  $searchBy      which field the search should go through. Default is all the fields (yomi is only available to ja-jp culture) [ex. searchBy=name or searchBy=displayname or searchBy=email or searchBy=yomi] 
     @param string  $culture         the culture context of the search; for instance japan is ja-jp; default is en-us [ex. culture=en-us] 
     @param string  $sortBy        Ways to sort the images; when excluded sortBy is all [ex. sortBy=popular or sortBy=recent]
     @param string  $sortOrder     Order of the image sorting which can be descending (default) or ascending [ex. sortOrder=asc] 
     @return object of python object representing the JSON in which the list of search
    """    
    def search_images(self, searchTerms, format=None, count=None,
                   startPage=None, culture=None, sortBy=None, sortOrder=None):
        return search.search_images( searchTerms, format, count,
                   startPage, culture, sortBy, sortOrder)
    
    
    """  Open Search
     Resource: http://api.myspace.com/opensearch/video?
     Details:  http://wiki.developer.myspace.com/index.php?title=Open_Search
     Description: Get Video Search
     @param mixed   $searchTerms   (mandatory parameter)search keywords
     @param integer $startIndex    Indicates the index of the first item to retrieve from the query set
     @param integer $count            total number of records
     @param string  $searchBy      which field the search should go through. Default is all the fields (yomi is only available to ja-jp culture) [ex. searchBy=name or searchBy=displayname or searchBy=email or searchBy=yomi] 
     @param string  $culture         the culture context of the search; for instance japan is ja-jp; default is en-us [ex. culture=en-us] 
     @param string  $tag           Determine if this is a tag search [ex. tag=1] 
     @param string  $videomode     Determine if this is a tag search [ex. videoMode=1 (music videos) or videoMode=2 (official)] 
     @return object of python object representing the JSON in which the list of search
    """      
    def search_videos(self, searchTerms, format=None, count=None,
                   startPage=None, culture=None, tag=None, videoMode=None):
        return   search.search_videos( searchTerms, format, count,
                   startPage, culture, tag, videoMode)
    
        
    
    """
    ------------------------------------------------------------------------------------------
    MySpace OpenSocial v0.9 REST Resources API wrapper functions
    http://wiki.developer.myspace.com/index.php?title=Category:OpenSocial_v0.9_REST_Resources  
    ------------------------------------------------------------------------------------------  
    """  
    
    
    """  OpenSocial v0.9 - Get Profile Comments        
        Resource:    http://opensocial.myspace.com/roa/09/profilecomments/@me/@self        
        Description: Return all comments available for user profile.
        Parameter:   @person_id (mandatory parameter) current person id e.g: @me
                     @fields (optional parameter). By default, the id of the comment author will be added 
                     to the result set, give the fields=author to get more information on the author
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_ProfileComments        
    """
    def get_profilecomments(self,person_id, fields=None):        
        return roaobj.get_profilecomments(person_id,fields)
    
    
    
    """ OpenSocial v0.9 - Retrieve all Album supported Fields        
       Resource:    http://opensocial.myspace.com/roa/09/albums/@supportedFields
       Description: Return all fields available for albums
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Albums
    """    
    def get_albumfields(self):       
        return roaobj.get_albumfields()



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
        return roaobj.get_albums(person_id, fields, startindex, count)
         
      
    
    
    """ OpenSocial v0.9 - Retrieve Album by ID       
       Resource:    http://opensocial.myspace.com/roa/09/albums/@me/@self/%s
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Albums
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @album_id (mandatory parameter)pass the  album id  which you want to get in response.
                    @fields  (optional) return fields which you need in response
       Description: get_albumbyidv9 return a specific album based on passed alumb_id    
    """
    def get_albumbyid(self,person_id, album_id, fields=None):            
        return roaobj.get_albumbyid(person_id, album_id, fields)
    
    

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
        return roaobj.create_album(person_id, caption, location, privacy) 
       
       
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
        return roaobj.update_album(person_id, album_id, caption, location, privacy)
    
    
    """ OpenSocial v0.9 - Retrieve all media item supported Fields 
       Resource:    http://opensocial.myspace.com/roa/09/mediaItems/@supportedFields      
       Description: Update album for with new values of parameters specified 
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """           
    def get_mediaitemfields(self):               
        return roaobj.get_mediaitemfields()   
    
 
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
        return roaobj.get_mediaitems(person_id, album_id, startindex, count)
    
    
    
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
        return roaobj.get_mediaitemsbymediaid(person_id,album_id, media_id)
    

    """ OpenSocial v0.9 - Get Media Items by Category
       Resource:    #http://opensocial.myspace.com/roa/09/mediaitems/{personId}/@videos/@supportedcategories
       Description: Retrieve MediaItem(Video) from suuported cat
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me                            
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """     
    def get_videocatergories(self, person_id): 
        return roaobj.get_videocatergories(person_id)
    
    """ OpenSocial v0.9 - Get Media Items by Category ID
       Resource:    #http://opensocial.myspace.com/roa/09/mediaitems/{personId}/@videos/@supportedcategories/{categoryId}
       Description: Retrieve MediaItem(Video) from suuported cat
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me                            
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """     
    def get_videocatergoriesbyid(self, person_id,cat_id):
        return roaobj.get_videocatergoriesbyid(person_id,cat_id)
    
    """ OpenSocial v0.9 - Get Media Item Fields
       Resource:    http://opensocial.myspace.com/roa/09/mediaItems/@supportedFields
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @album_id (madator parameter)Id of album which you want to update
                    @caption (Optional parameter)use in place of title. 
                    @location (optional parameter) 
                    @privacy  (optional parameter) specifies visibility for album, 
                    it can be one of 'Everyone', 'FriendsOnly' or 'Me' 
       Description: Update album for with new values of parameters specified 
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """      
    
    def add_photoalbum(self,person_id,caption,album_id,data):
         return roaobj.add_photoalbum(person_id,caption,album_id,data)        
  
  
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
    def add_videotoalbum(self,person_id,album_id,caption,description,tags,language,data,mscategories):
        #return roaobj.add_photoalbum(data)
        return roaobj.add_video(person_id,album_id,caption,description,tags,language,data,mscategories)
       

    """ OpenSocial v0.9 MediaItemComments
       Resource:    http://opensocial.myspace.com/roa/09/mediaitemcomments/{personId}/@self/{albumId}/{mediaItemId}
       Description: Get comments associated with media item, based on album_id and media_id
       Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                    @album_id (mandatory parameter)Id of album which you want to update
                    @media_id (mandatory parameter)Id of media items for which you want to get data                    
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_MediaItemComments           
    """          
    def get_mediaitemscomments(self,person_id, album_id, media_id):   
        return roaobj.get_mediaitemscomments(person_id, album_id, media_id)
    
    
    """ OpenSocial v0.9 - Retrieve all activity supported Fields 
       Resource:    http://opensocial.myspace.com/roa/09/activities/@supportedFields    
       Description: Retrieve all activity supported fields
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """   
    def get_activitiesfields(self):
        return roaobj.get_activitiesfields() 
         
   
    """ OpenSocial v0.9 - Retrieve all supported verbs 
       Resource:    http://opensocial.myspace.com/roa/09/activities/@supportedVerbs       
       Description: Retrieve all activity supported verbs
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """   
    def get_activitiesverbs(self):                
        return roaobj.get_activitiesverbs()  
    
    
    """ OpenSocial v0.9 - Retrieve all supported Object Types 
       Resource:    http://opensocial.myspace.com/roa/09/activities/@supportedObjectTypes      
       Description: Retrieve all activity supported Object Types
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_0.9_MediaItems            
    """   
    def get_activitiesobjecttypes(self):               
        return roaobj.get_activitiesobjecttypes()   
    
    
    """ The function will get all of the activites of a given user, provided that the current user and application have privilages to access it
   
     @param int|string $userId
     @param unknown_type $culture
     @param mixed $datetime A better limit on the activities returned is datetime because it allows the consumer to query 
                            deltas and only processed what has changed. Pass a date that is less than 60 days ago as the maximum and default number of days back you can query is 60. 
                            If you query more than that the system will only go as far back as 60. Example of querystring parameters is: datetime=06/21/2009
    
     @param string $activityTypes PhotoTagged|PhotoAdd|SongUpload|ProfileSongAdd|BlogAdd|ForumPosted|ForumTopicReply|VideoAdd|ProfileVideoUpdate|FavoriteVideoAdd|FriendAdd|JoinedGroup|FriendCategoryAdd|PersonalBandShowUpdate|EventPosting|EventAttending|ApplicationAdd
     @param int    $pageSize      You can use this parameter to specify the number of atom entries returned in the stream
     @param bool   $composite      Set this parameter to true t
     @param bool   $composite      Set this parameter to true to get one atom entry for all activities of the same type on the same day. If the objects of the activities go into targets then they will be grouped by target. Ex: Max uploaded 5 photos into the album Medieval Times.
     @param bool   $extensions    Pipe delimited list of options syndicating the activity stream. Name fo the query string parameter is "extensions" Example: &extensions=actor|subject
    
     @return SimpleXML a SimpleXML representation of an Activities ATOM Feed
    """
    def get_activities(self, user_id,activitytypes=None,culture=None,datetime=None,composite=None,extensions=None,page_size=None):        
        return restv1obj.get_activities_atom( user_id,activitytypes,culture,datetime,composite,extensions,page_size)
    
    
    """ The function will get all of the activites of a user friend, provided that the current user and application have privilages to access it
   
     @param int|string $userId
     @param unknown_type $culture
     @param mixed $datetime A better limit on the activities returned is datetime because it allows the consumer to query 
                            deltas and only processed what has changed. Pass a date that is less than 60 days ago as the maximum and default number of days back you can query is 60. 
                            If you query more than that the system will only go as far back as 60. Example of querystring parameters is: datetime=06/21/2009
    
     @param string $activityTypes PhotoTagged|PhotoAdd|SongUpload|ProfileSongAdd|BlogAdd|ForumPosted|ForumTopicReply|VideoAdd|ProfileVideoUpdate|FavoriteVideoAdd|FriendAdd|JoinedGroup|FriendCategoryAdd|PersonalBandShowUpdate|EventPosting|EventAttending|ApplicationAdd
     @param int    $pageSize      You can use this parameter to specify the number of atom entries returned in the stream
     @param bool   $composite      Set this parameter to true t
     @param bool   $composite      Set this parameter to true to get one atom entry for all activities of the same type on the same day. If the objects of the activities go into targets then they will be grouped by target. Ex: Max uploaded 5 photos into the album Medieval Times.
     @param bool   $extensions    Pipe delimited list of options syndicating the activity stream. Name fo the query string parameter is "extensions" Example: &extensions=actor|subject
    
     @return SimpleXML a SimpleXML representation of an Activities ATOM Feed
    """
    def get_friends_activities(self, user_id,activitytypes=None,culture=None,datetime=None,composite=None,extensions=None,page_size=None):
        return restv1obj.get_friends_activities_atom( user_id,activitytypes,culture,datetime,composite,extensions,page_size)
    
          
     
    
    
    
    
    """ OpenSocial v0.9 - Retrieve viewer activities by appID 
        Resource:    http://opensocial.myspace.com/roa/09/activities/{personId}/{selector}       
        Description: Return all activities available for viewer for an appID specified in parameter
        Parameter:   @app_id (mandatory parameter) refers to applicaiton id for which user wants to check activities
                     @fields (optional parameter).------------------------------                     
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Activities        
    """
    def get_activitiesbyappid(self,person_id, app_id, fields=None):
        return roaobj.get_activitiesbyappid(person_id, app_id, fields)
    
    

    
    
    """ OpenSocial v0.9 - Retrieve friend activities by appID 
        Resource:    http://opensocial.myspace.com/roa/09/activities/{personId}/{selector}       
        Description: Return all activities available for friend for an appID specified in parameter
        Parameter:   @person_id (mandatory parameter) current person id e.g: @me
                     @app_id (mandatory parameter) refers to applicaiton id for which user wants to check activities    
                     @fields (optional parameter).specific fields
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Activities        
    """
    def get_friendactivitiesbyappid(self, person_id, app_id, fields=None):
        return roaobj.get_friendactivitiesbyappid(person_id, app_id, fields)
    
    
    #def create_activity9(self, title,nobody,templateid,templateparams):
    def create_activity(self,person_id,external_id,title,body,templateparams, title_id):
        return roaobj.create_activity(person_id,external_id,title,body,templateparams, title_id)
           
           

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
        return roaobj.get_appdata( person_id,app_id , fields)
    
    
    
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
      return roaobj.add_appdata( person_id, app_id, key, value) 



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
        return roaobj.update_appdata(person_id, app_id, key, value)
     
     
     
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
        return roaobj.delete_appdata(person_id,app_id, fields) 
              
     
    """ OpenSocial v0.9 Groups- Retrieve all supported fields   
       Resource:    http://opensocial.myspace.com/roa/09/groups/@supportedFields       
       Description: Retrieve all group supported fields
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_Groups           
    """         
    def get_groupfields(self):
        return roaobj.get_groupfields()   
    

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
        return roaobj.get_groups(person_id, startindex, count) 
    

    """ OpenSocial v0.9 People- Retrieve all supported fields   
       Resource:    http://opensocial.myspace.com/roa/09/people/@supportedFields        
       Description: Retrieve all people supported fields
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_People           
    """ 
    def get_peoplefields(self):
        return roaobj.get_peoplefields()     
    
    
    
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
        return roaobj.get_person(person_id, fields, filterby, filterop, filtervalue,
                     format, startindex, count)
    
    
    
    
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
         return roaobj.get_friends(person_id, fields, filterby, filterop, filtervalue,
                     format, startindex, count)
    
    
    
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
        return roaobj.get_peoplebyfriendid(person_id, friend_id, fields=None) 
    
    
    
    """OpenSocial v0.9 StatusMood - Retrieve all supported moods    
       Resource:    http://opensocial.myspace.com/roa/09/statusmood/@me/@supportedMood      
       Description: Retrieve all supported moods 
       Parameters:  person_id (mandatory parameter) current person id e.g: @me                       
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood          
    """   
    def get_supportedsmoods(self,person_id):           
        return roaobj.get_supportedsmoods(person_id)
    
    
    """OpenSocial v0.9 StatusMood - Retrieve all supported moods by id 
       Resource:    http://opensocial.myspace.com/roa/09/statusmood/{personId}/@supportedMood/{moodId}      
       Description: Retrieve all supported moods by id  
       Parameters:  person_id (mandatory parameter) current person id e.g: @me       
                    mood_id (Optional parameter) id of mood which you want to retrive                
       Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood          
    """   
    def get_supportedsmoodbyid(self,person_id, mood_id=None):
        return roaobj.get_supportedsmoodbyid(person_id, mood_id)
    
    
    """ OpenSocial v0.9 Retrieve a status & mood for user
        Resource:    http://opensocial.myspace.com/roa/09/statusmood/{personId}/{selector}
        Description: Retrieve a status & mood for user
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me 
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood
    """
    def get_statusmood(self,person_id):
        return roaobj.get_statusmood(person_id)

  
       
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
        return roaobj.get_friendstatusmood(person_id, filterby, filterop, filtervalue, includeself,
                              culture, fields)
    
   
    """ OpenSocial v0.9 Retrieve a status & mood history for user
        Resource:    http://opensocial.myspace.com/roa/09/statusmood/{personId}/{selector}/history 
        Description: Retrieve a status & mood history for user
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me 
                     @fields (optional parameter) specific fields
        Details:     http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMood
    """
    def get_selfstatusmoodhistory(self,person_id, fields=None):
        return roaobj.get_selfstatusmoodhistory(person_id, fields)
   
   

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
        return roaobj.get_friendstatusmoodhistory(person_id, filterby, filterop, filtervalue, includeself,
                              culture, fields, startIndex, itemsPerPage)


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
        return roaobj.get_statusmoodbyfriendid(person_id, friend_id, filterby, filterop, filtervalue, includeself,
                              culture, fields, startIndex, itemsPerPage)    
    
    
    
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
        return roaobj.get_statusmoodhistorybyfriendid(person_id, friend_id, filterby, filterop, filtervalue, includeself,
                              culture, fields, startIndex, itemsPerPage)    
     
     
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
        return roaobj.set_status(person_id, latitude, longitude, moodname, status)


   
    """ OpenSocial v0.9 Get StatusMoodComments
        Resource:    http://opensocial.myspace.com/roa/09/statusmoodcomments/{personId}/@self  
        Description: Get all Status mood comments
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me                                    
        Details:    http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMoodComments
    """     
    def get_statusmoodcomments(self,person_id,status_id):  
        return roaobj.get_statusmoodcomments(person_id,status_id)
    
  
    """ OpenSocial v0.9 Set StatusMoodComments
        Resource:    #http://opensocial.myspace.com/roa/09/statusmoodcomments/{personId}/@self?statusId={statusId} 
        Description: Set Status mood comments for a particular s
        Parameters:  @person_id (mandatory parameter) current person id e.g: @me
                     @body (mandatory parameter) body of status comment
                     @statusid(mandatory paramter) id of parameter for which comment is posted                                    
        Details:    http://wiki.developer.myspace.com/index.php?title=OpenSocial_v0.9_StatusMoodComments
    """   
    def set_statusmoodcomments(self,person_id, body, status_id):
        return roaobj.set_statusmoodcomments(person_id, body, status_id)

 
    """OpenSocial v0.9 Notifications
        send_notification Usage:
        
        ms = MySpace(ckeynsecret.CONSUMER_KEY, ckeynsecret.CONSUMER_SECRET)
          templateparam ='[{"key":"content","value":"Test notification content from python sdk"},\
                                {"key":"button0_surface","value":"canvas"},\
                                {"key":"button0_label","value":"Go To App Canvas"},\
                                {"key":"button1_label","value":"Go To App Profile"}]'
              notification_data = ms.send_notification(person_id="333220680", recipientids="333220680", templateparams=templateparam, mediaitems='http://opensocial.myspace.com/roa/09/mediaitemcomments/333220680/@self')
              
    """
    #def send_onotification(self, recipients, content, btn0_label=None, btn0_surface=None, btn1_label=None, btn1_surface=None, mediaitems=None):
   #def send_notificationv9(self,person_id, btn0_label=None, btn0_surface=None, btn1_label=None, btn1_surface=None, mediaitems=None):
    def send_notification(self,person_id, recipientids, templateparams, mediaitems):
        return roaobj.send_notification(person_id, recipientids, templateparams, mediaitems)
    

    """ Real Time Stream
        Resource:     http://api.myspace.com/stream/subscription? 
        Description: Add Subscription
        Subscription Usage : addSubscriptionV9('All','http://myspace.mycompany.com/handler.ashx','{}','',1,1);                                  
        Details:    http://wiki.developer.myspace.com/index.php?title=Category:Real_Time_Stream
    """       
    def add_subscription(self, type, endpoint, query, metadata, batchsize, rate, format, addlist, removelist):    
        return realtimeobj.add_subscription(type, endpoint, query, metadata, batchsize, rate, format, addlist, removelist) 
       

    """ Real Time Stream
        Resource:     http://api.myspace.com/stream/subscription/{subscriptionId}? 
        Description: Update subscription
        Update Subscription Usage : updateSubscriptionV9('1234', 'All','http://myspace.mycompany.com/handler.ashx','{}','',1,1);                                  
        Details:    http://wiki.developer.myspace.com/index.php?title=Category:Real_Time_Stream
    """ 
    def update_subscription(self, subcriptionid, type, endpoint, query, metadata, batchsize, rate, format, addlist, removelist):
        return realtimeobj.update_subscription(subcriptionid, type, endpoint, query, metadata, batchsize, rate, format, addlist, removelist) 

    """ Real Time Stream
        Resource:      http://api.myspace.com/stream/subscription/{subscriptionId}? 
        Description: Delete Subscription
        Parameter:  subcription_id (mandatory) id of subscrption which user want to delete                                  
        Details:    http://wiki.developer.myspace.com/index.php?title=Category:Real_Time_Stream
    """ 
    def delete_subscription(self, subscription_id):   
        return realtimeobj.delete_subscription(subscription_id) 
       
    """ Real Time Stream
        Resource:      http://api.myspace.com/stream/subscription/{subscriptionId}? 
        Description: Get Subscption 
        Parameter:  subcription_id (mandatory) id of subscrption which user want to Get                                  
        Details:    http://wiki.developer.myspace.com/index.php?title=Category:Real_Time_Stream
    """  
    def get_subscription(self, subscription_id):   
        return realtimeobj.get_subscription(subscription_id)        
           
    

    """ Real Time Stream
        Resource:   http://api.myspace.com/stream/subscription/{all}? 
        Description:Delete all Subscription                                       
        Details:    http://wiki.developer.myspace.com/index.php?title=Category:Real_Time_Stream
    """ 
    def delete_allsubscription(self):
        return realtimeobj.delete_allsubscription() 
       
    """ Real Time Stream
        Resource:   http://api.myspace.com/stream/subscription/{subscriptionId}? 
        Description:Get all Subscption                                         
        Details:    http://wiki.developer.myspace.com/index.php?title=Category:Real_Time_Stream
    """  
    def get_allsubscription(self):   
        return realtimeobj.get_allsubscription()
    
        
     
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
       return pocoobj.get_personpoco(person_id, page, page_size, fields)    
    
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
        return pocoobj.get_friendspoco(person_id, page, page_size) 
    
    def get_friendship(self, user_id, friend_ids):
        return restv1obj.get_friendship(user_id,friend_ids)
    
    def get_indicators(self, user_id):        
        return restv1obj.get_indicators(user_id)
    
    def get_globalappdata(self, keys=None):        
        return restv1obj.get_globalappdata(keys)
    
    def add_globalappdata(self, keys):         
        return restv1obj.add_globalappdata(keys)
    
    