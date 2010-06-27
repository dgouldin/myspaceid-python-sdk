
import string
from myspace.config.MySpaceError import MySpaceError

#rest v1

API_ALBUMS_URL = 'http://api.myspace.com/v1/users/%s/albums.json'
API_ALBUM_URL = 'http://api.myspace.com/v1/users/%s/albums/%s/photos.json'
API_FRIENDS_URL = 'http://api.myspace.com/v1/users/%s/friends.json'
API_FRIENDSHIP_URL = 'http://api.myspace.com/v1/users/%s/friends/%s.json'
API_MOOD_URL = 'http://api.myspace.com/v1/users/%s/mood.json'
API_MOODS_URL = 'http://api.myspace.com/v1/users/%s/moods.json'
API_PHOTOS_URL = 'http://api.myspace.com/v1/users/%s/photos.json'
API_PHOTO_URL = 'http://api.myspace.com/v1/users/%s/photos/%s.json'
API_PROFILE_URL = 'http://api.myspace.com/v1/users/%s/profile.json'
API_STATUS_URL = 'http://api.myspace.com/v1/users/%s/status.json'
API_VIDEOS_URL = 'http://api.myspace.com/v1/users/%s/videos.json'
API_VIDEO_URL = 'http://api.myspace.com/v1/users/%s/videos/%s.json'
API_ACTIVITIES_URL = "http://api.myspace.com/v1/users/%s/activities.atom"
API_FRIENDSACTIVITIES_URL = "http://api.myspace.com/v1/users/%s/friends/activities.atom"
API_UPDATE_STATUS_URL = "http://api.myspace.com/v1/users/%s/status";
API_UPDATE_MOOD_URL = "http://api.myspace.com/v1/users/%s/mood";
API_CREATE_ALBUM_URL = 'http://api.myspace.com/v1/users/%s/albums.json'
API_INDICATORS_URL = 'http://api.myspace.com/v1/users/%s/indicators.json'
API_NOTIFICATIONS_URL = 'http://api.myspace.com/v1/applications/%s/notifications'
API_GLOBALAPPDATA_URL = 'http://api.myspace.com/v1/appdata/global.json' 
API_FRIENDSLIST_URL = 'http://api.myspace.com/v1/users/%s/friendslist/%.json'
API_USERFRIENDSTATUS_URL = 'http://api.myspace.com/v1/users/%s/friends/status.json'
API_COMMENTS_URL = 'http://api.myspace.com/v1/users/%s/comments.json'

class RestV1():    
    def __init__(self,objmyspacecontext):
        global context
        context= objmyspacecontext    
    
    def get_albums(self, user_id, page=None, page_size=None):
        context.validate_params(locals())
        albums_request_url = API_ALBUMS_URL % user_id
        #set up extra params, if any
        params = {}
        if page is not None:
            params['page'] = page
        if page_size is not None:
            params['page_size'] = page_size
        return context.callmyspaceapi(albums_request_url, parameters=params)
    
    def get_album(self, user_id, album_id):
        context.validate_params(locals())
        album_request_url = API_ALBUM_URL % (user_id, album_id)
        return context.callmyspaceapi(album_request_url)
    
    def get_friends(self, user_id, page=None, page_size=None, list=None, show=None):
        # validate common parameters
        context.validate_params(locals())
        #validate the list param - it can be one of 'top', 'online' or 'app'
        valid_list_values = ['top', 'online', 'app']
        if list is not None:
            if list not in valid_list_values:
                raise MySpaceError('Invalid Parameter Value. list must be one of %s' % str(valid_list_values))
                return
        #validate show parameter. show can be a combination of 'mood', 'status', 'online' separated by '|'
        valid_show_values = ['mood', 'status', 'online']
        if show is not None:
            given_show = string.split(show, '|')
            for s in given_show:
                if s not in valid_show_values:
                    raise MySpaceError('Invalid Parameter Value. show must be a combination of %s' % str(valid_show_values))
                    return
        # Proceed to making the request
        friends_request_url = API_FRIENDS_URL % user_id       
        #set up extra params, if any
        params = {}
        if page is not None:
            params['page'] = page
        if page_size is not None:
            params['page_size'] = page_size
        if list is not None:
            params['list'] = list
        if show is not None:
            params['show'] = show             
        return context.callmyspaceapi(friends_request_url, parameters=params)

    def get_friendslist(self, user_id, friend_ids, show=None):
        
        # validate common parameters
        context.validate_params(locals())
    
        #validate show parameter. show can be a combination of 'mood', 'status', 'online' separated by '|'
        valid_show_values = ['mood', 'status', 'online']
        if show is not None:
            given_show = string.split(show, '|')
            for s in given_show:
                if s not in valid_show_values:
                    raise MySpaceError('Invalid Parameter Value. show must be a combination of %s' % str(valid_show_values))
                    return
        # Proceed to making the request
        
        friendslist_request_url = API_FRIENDSLIST_URL % (user_id, friend_ids)  
        #set up extra params, if any
        params = {}
        
        if show is not None:
            params['show'] = show      
        
        #return friendslist_request_url
         
        #TODO
        #Response NOT TESTED YET           
        return context.callmyspaceapi(friendslist_request_url, parameters=params) 

    def get_friendship(self, user_id, friend_ids):
        context.validate_params(locals())
        friendship_request_url = API_FRIENDSHIP_URL % (user_id, friend_ids)
        return context.callmyspaceapi(friendship_request_url)

    def get_comments(self, user_id, page=None, page_size=None):
        context.validate_params(locals())
        comments_request_url = API_COMMENTS_URL % user_id
        #set up extra params, if any
        params = {}
        if page is not None:
            params['page'] = page
        if page_size is not None:
            params['page_size'] = page_size
        
        return context.callmyspaceapi(comments_request_url, parameters=params)
    
       
    def get_mood(self, user_id):
        context.validate_params(locals())
        mood_request_url = API_MOOD_URL % user_id
        return context.callmyspaceapi(mood_request_url)

    def get_moods(self, user_id):
        context.validate_params(locals())
        moods_request_url = API_MOODS_URL % user_id
        return context.callmyspaceapi(moods_request_url)

    def get_photos(self, user_id, page=None, page_size=None):
        context.validate_params(locals())
        photos_request_url = API_PHOTOS_URL % user_id       
        #set up extra params, if any
        params = {}
        if page is not None:
            params['page'] = page
        if page_size is not None:
            params['page_size'] = page_size            
        return context.callmyspaceapi(photos_request_url, parameters=params)

    def get_photo(self, user_id, photo_id):
        context.validate_params(locals())
        photo_request_url = API_PHOTO_URL % (user_id, photo_id)
        return context.callmyspaceapi(photo_request_url)
    
    def get_profile(self, user_id, type='full'):        
        #objmyspacecontext.__validate_params(locals())
        #validate the type param - it can be one of 'basic', 'full' or 'extended'
        valid_type_values = ['basic', 'full', 'extended']
        if type is not None:
            if type not in valid_type_values:
                raise MySpaceError('Invalid Parameter Value. list must be one of %s' % str(valid_type_values))
                return
     
        params = {}
        params['detailtype'] = type
        
        profile_request_url = API_PROFILE_URL % user_id
        return context.callmyspaceapi(profile_request_url, parameters=params)

    def get_profile_basic(self, user_id):
        return self.get_profile(user_id, type='basic')

    def get_profile_full(self, user_id):
        return self.get_profile(user_id, type='full')

    def get_profile_extended(self, user_id):
        return self.get_profile(user_id, type='extended')
    
    def get_status(self, user_id):
        context.validate_params(locals())
        status_request_url = API_STATUS_URL % user_id
        return context.callmyspaceapi(status_request_url)

    def get_videos(self, user_id):
        context.validate_params(locals())
        videos_request_url = API_VIDEOS_URL % user_id
        return context.callmyspaceapi(videos_request_url)

    def get_video(self, user_id, video_id):
        context.validate_params(locals())
        video_request_url = API_VIDEO_URL % (user_id, video_id)
        return context.callmyspaceapi(video_request_url)
    
    
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
    def get_activities_atom(self, user_id,activitytypes=None,culture=None,datetime=None,composite=None,extensions=None,page_size=None):
        context.validate_params(locals())
        
        params = {}
        if activitytypes is not None:
            params["activitytypes"] = activitytypes        
        if extensions is not None:
            params["extensions"] = extensions        
        if page_size is not None:
            params["page_size"] = page_size            
        if culture is not None:
            params["culture"] = culture            
        if datetime is not None:
            params["datetime"] = datetime
        if composite is not None:
            composite["composite"] = datetime
                
        activities_request_url = API_ACTIVITIES_URL % user_id
        
        
        return context.callmyspaceapi(activities_request_url,parameters=params, get_raw_response=True)

    def get_friends_activities_atom(self, user_id,activitytypes=None,culture=None,datetime=None,composite=None,extensions=None,page_size=None):
        context.validate_params(locals())
        
        params = {}
        if activitytypes is not None:
            params["activitytypes"] = activitytypes        
        if extensions is not None:
            params["extensions"] = extensions        
        if page_size is not None:
            params["page_size"] = page_size            
        if culture is not None:
            params["culture"] = culture            
        if datetime is not None:
            params["datetime"] = datetime
        if composite is not None:
            composite["composite"] = datetime
            
        activities_request_url = API_FRIENDSACTIVITIES_URL % user_id
        
        return context.callmyspaceapi(activities_request_url, get_raw_response=True)

    def set_status(self, user_id, status):
        context.validate_params(locals())
        if len(status) == 0:
            raise MySpaceError('status must be set to a non-empty string')
            return
        params = {}
        params['status'] = status
        update_status_url = API_UPDATE_STATUS_URL % user_id
        # setting get_raw_status=True since the REST API does not return any data on success
        return context.callmyspaceapi(update_status_url, method='PUT', parameters=params, get_raw_response=True)

    def set_mood(self, user_id, mood):
        context.validate_params(locals())
        params = {}
        params['mood'] = mood
        update_mood_url = API_UPDATE_MOOD_URL % user_id
        # setting get_raw_status=True since the REST API does not return any data on success
        return context.callmyspaceapi(update_mood_url, method='PUT', parameters=params, get_raw_response=True)

    def create_album(self, user_id, title, location=None, privacy='Everyone'):
        context.validate_params(locals())
        #validate the privacy param - it can be one of 'Everyone', 'FriendsOnly' or 'Me'
        valid_privacy_values = ['Everyone', 'FriendsOnly', 'Me']
        if privacy is not None:
            if privacy not in valid_privacy_values:
                raise MySpaceError('Invalid Parameter Value. list must be one of %s' % str(valid_privacy_values))
                return
        album_create_url = API_CREATE_ALBUM_URL % user_id
        # set up album location, title etc.
        params = {}
        params['title'] = title
        if privacy is not None:
            params['privacy'] = privacy
        if location is not None:
            params['location'] = location
        return context.callmyspaceapi(album_create_url, method='POST', parameters=params)

    def get_indicators(self, user_id):
        context.validate_params(locals())
        get_indicators_url = API_INDICATORS_URL % user_id
        return context.callmyspaceapi(get_indicators_url)

    """
        send_notification Usage:
        
        ms = MySpace(ckeynsecret.CONSUMER_KEY, ckeynsecret.CONSUMER_SECRET)
        notification_data = ms.send_notification(135455, "296768296", "Test Notification With A Button", 
                                                 btn0_label="Go To Canvas", btn0_surface="canvas",
                                                 btn1_label="Go To App Profile", btn1_surface="appProfile",
                                                 mediaitems="http://api.myspace.com/v1/users/296768296")  
    """
    def send_notification(self, app_id, recipients, content, btn0_label=None, btn0_surface=None, btn1_label=None, btn1_surface=None, mediaitems=None):
        context.validate_params(locals())
        if len(recipients) == 0:
           raise MySpaceError('recipients must be set to a non-empty string')
           return
        if len(content) == 0:
           raise MySpaceError('content must be set to a non-empty string')
           return

        params = {}
        params['recipients'] = recipients

        templateParameters = '{"content":"' + content + '"'
        if btn0_label is not None:
          if len(btn0_label) != 0:
             templateParameters += ',"button0_label":"' + btn0_label + '"' + ',"button0_surface":"' + btn0_surface + '"'
        if btn1_label is not None:
          if len(btn1_label) != 0:
             templateParameters += ',"button1_label":"' + btn1_label + '"' + ',"button1_surface":"' + btn1_surface + '"'
        templateParameters += '}'
        params['templateParameters'] = templateParameters

        if mediaitems is not None:
          if len(mediaitems) != 0:
             params['mediaitems'] = '{"' + mediaitems + '"}'     
        
        send_notification_url = API_NOTIFICATIONS_URL % app_id
        return context.callmyspaceapi(send_notification_url, method='POST', parameters=params)
    
    def get_globalappdata(self, keys=None):        
        params = {}      
        if keys is not None:
             params['keys'] = keys
        appdata_url = API_GLOBALAPPDATA_URL
        return context.callmyspaceapi(appdata_url)
    
    def add_globalappdata(self, keys):        
        params = {}      
        if keys is not None:
             params['keys'] = keys
        appdata_url = API_GLOBALAPPDATA_URL
        return context.callmyspaceapi(appdata_url,method="POST", parameters=params)
