import simplejson
import unittest

from myspace.myspaceapi import MySpace
from myspace.config import MySpaceError
from myspace.context import MySpaceContext

class ApiParameterValidationTest(unittest.TestCase):

  def setUp(self):
      
      self.ms = MySpace ('KEY HERE', 'SECRET HERE',oauth_token_key='TOKEN HERE',oauth_token_secret='TOKEN SCREET HERE')
      self.appid = 'APP ID HERE'

  
  def test_call_apis_with_negative_params(self):
      """Tests the calling of methods on the MySpace object by specifying negative param values. 
      """
      user_id = page = page_size = album_id = friend_ids = photo_id = video_id = -1

      """self.assertRaises(MySpaceError, self.ms.get_albums, user_id)
      self.assertRaises(MySpaceError, self.ms.get_album, user_id, album_id)
      self.assertRaises(MySpaceError, self.ms.get_friends, user_id, page=page, page_size=page_size)
      self.assertRaises(MySpaceError, self.ms.get_friendship, user_id, friend_ids)
      self.assertRaises(MySpaceError, self.ms.get_mood, user_id)
      self.assertRaises(MySpaceError, self.ms.get_photos, user_id, page=page, page_size=page_size)
      self.assertRaises(MySpaceError, self.ms.get_photo, user_id, photo_id)
      self.assertRaises(MySpaceError, self.ms.get_profile, user_id)
      self.assertRaises(MySpaceError, self.ms.get_status, user_id)
      self.assertRaises(MySpaceError, self.ms.get_videos, user_id)
      self.assertRaises(MySpaceError, self.ms.get_video, user_id, video_id)"""




#def get_albumfieldsv9(self):
  def test_get_albumfields(self):
      """Tests the calling of get_albumfields          
      """         
      result = self.ms.get_albumfields()      
      self.assertTrue(len(result)>0)
      


#def get_albumsv9(self,person_id, fields=None, startindex=None, count=None):
  def test_get_albums_wp(self):
      """Tests the calling of get_albums with an invalid value for the personid parameter         
      """
      person_id=123456
      self.assertRaises(MySpaceError,self.ms.get_albums,person_id)



#def get_albumsv9(self,person_id, fields=None, startindex=None, count=None):
  def test_get_albums(self):
      """Tests the calling of get_albums with a valid value for the personid parameter         
      """
      person_id = '@me'
      result = self.ms.get_albums(person_id)      
      self.assertTrue(len(result)>0)
      
      
      
#def get_albumbyidv9(self,person_id, album_id, fields=None):     
  def test_get_albumbyid_wp(self):
      """Tests the calling of get_albumbyid with an invalid value for the personid parameter         
      """
      person_id=123456
      album_id = 123456
      self.assertRaises(MySpaceError,self.ms.get_albumbyid,person_id,album_id)
      
  def test_get_albumbyid(self):
      """Tests the calling of get_albumbyid with a valid value for the personid,albumid parameter         
      """
      person_id="@me"
      result = self.ms.get_albums(person_id)      
      album_id = result["entry"][0]["album"]["id"]
      count = self.ms.get_albumbyid(person_id,album_id)
  
      self.assertTrue(len(count)>0)
      
       
#def create_albumv9(self,person_id, caption, location=None, privacy='Everyone'):
  def test_create_album_wp(self):
      """Tests the calling of create_album with an invalid value for the personid parameter         
      """
      person_id = 123456
      self.assertRaises(MySpaceError,self.ms.create_album,person_id,"Test Caption")
  
  def test_create_album(self):
      """Tests the calling of create_album with a valid value for the personid parameter         
      """
      person_id = "@me"
      statuslink = self.ms.create_album(person_id, caption="TEST")
      self.failIfEqual(None,statuslink,"Error")
      


#def update_albumv9(self,person_id, album_id, caption=None, location=None, privacy='Everyone'):
  def test_update_album_wp(self):
      """Tests the calling of update_album with an invalid value for the personid parameter         
      """
      person_id = 123456
      album_id = 0      
      self.assertRaises(MySpaceError,self.ms.update_album,person_id,"Test Caption",album_id,privacy="junk")


  def test_update_album(self):
      """Tests the calling of update_album with a valid value for the personid and albumid         
      """
           
      person_id="@me"
      result = self.ms.get_albums(person_id)      
      album_id = result["entry"][0]["album"]["id"]
      statuslink = self.ms.update_album(person_id,album_id,caption="updated caption")  
      self.failIfEqual(None,statuslink,"Error")
      
      
  
#def get_mediaitemfieldsv9(self):
  def test_get_mediaitemfields(self):
      """Tests the calling of get_mediaitemfields          
      """
      result = self.ms.get_mediaitemfields()      
      self.assertTrue(len(result)>0)
      
  
#def get_mediaitemsv9(self,person_id, album_id, startindex=None, count=None):
  def test_get_mediaitems_wp(self):
      """Tests the calling of get_mediaitems with an invalid value of personid parameter         
      """
      person_id = 123456
      album_id = 0      
      self.assertRaises(MySpaceError,self.ms.get_mediaitems,person_id,album_id)    
      
  def test_get_mediaitems(self):
      """Tests the calling of get_mediaitems with a valid value of personid and albumid parameter         
      """
      person_id="@me"
      result = self.ms.get_albums(person_id)      
      album_id = result["entry"][0]["album"]["id"]
      mediaresult = self.ms.get_mediaitems(person_id,album_id)
      self.assertTrue(len(mediaresult)>0)     
        
      
#def get_mediaitemsbymediaidv9(self, person_id,album_id, media_id):  
  def test_get_mediaitemsbymediaid_wp(self):
      """Tests the calling of get_mediaitemsbymediaid with an invalid value of personid,
      albumid and mediaid parameter         
      """
      person_id = 123456
      album_id = 0
      media_id = 123      
      self.assertRaises(MySpaceError,self.ms.get_mediaitemsbymediaid,person_id,album_id,media_id)  


  def test_get_mediaitemsbymediaid(self):
      """Tests the calling of get_mediaitemsbymediaid with a valid value of personid,
      albumid and mediaid parameter         
      """
      person_id="@me"
      result = self.ms.get_albums(person_id)      
      album_id = result["entry"][0]["album"]["id"]
      mediaresult = self.ms.get_mediaitems(person_id,album_id)
      if  mediaresult["entry"] is not None:    
          media_id = mediaresult["entry"][0]["mediaItem"]["id"]
          resultitem = self.ms.get_mediaitemsbymediaid(person_id,album_id,media_id)
          self.assertTrue(len(resultitem)>0) 
        
       
#def add_photoalbum(self,data):  


#def get_mediaitemscommentsv9(self,person_id, album_id, media_id): 
  def test_get_mediaitemscomments_wp(self):
      """Tests the calling of get_mediaitemscomments with an invalid value of personid,
      albumid and mediaid parameter         
      """
      person_id = 123456
      album_id = 0
      media_id = 123      
      self.assertRaises(MySpaceError,self.ms.get_mediaitemscomments,person_id,album_id,media_id)  
  
  def test_get_mediaitemscomments(self):
      """Tests the calling of get_mediaitemscomments with an invalid value of personid,
      albumid and mediaid parameter         
      """
      person_id="@me"
      result = self.ms.get_albums(person_id)      
      album_id = result["entry"][0]["album"]["id"]
      mediaresult = self.ms.get_mediaitems(person_id,album_id)
      if  mediaresult["entry"] is not None:    
          media_id = mediaresult["entry"][0]["mediaItem"]["id"]
          resultitem = self.ms.get_mediaitemscomments(person_id,album_id,media_id)          
          self.assertTrue(len(resultitem)>=0)   
     

#def get_activitiesfieldsv9(self):
  def test_get_activitiesfields(self):
      """Tests the calling of get_activitiesfields       
      """         
      result = self.ms.get_activitiesfields()
      self.assertTrue(len(result)>0)
     
 
#def get_activitiesverbsv9(self):
  def test_get_activitiesverbs(self):
      """Tests the calling of get_activitiesverbs       
      """         
      result = self.ms.get_activitiesverbs()
      self.assertTrue(len(result)>0)
      
#def get_activitiesobjecttypesv9(self):
  def test_get_activitiesobjecttypes(self):
      """Tests the calling of get_activitiesobjecttypes       
      """         
      result = self.ms.get_activitiesobjecttypes()
      self.assertTrue(len(result)>0)
      

#def get_activitiesv9(self,person_id, fields=None):
  def test_get_activities_wp(self):
      """Tests the calling of get_activities with an invalid value of personid,
      parameter         
      """
      person_id = 123456     
      self.assertRaises(MySpaceError,self.ms.get_activities,person_id)
      

  def test_get_activities(self):
      """Tests the calling of get_activities with a valid value of personid,
      parameter         
      """
      person_id = self.ms.get_userid()    
      result = self.ms.get_activities(person_id)
      self.assertTrue(len(result)>=0)
        
       

#def get_activitiesbyappidv9(self,person_id, app_id, fields=None):
  def test_get_activitiesbyappid_wp(self):
      """Tests the calling of get_activitiesbyappid with an invalid value of personid
      and appid parameters         
      """
      person_id = 123456
      app_id = 123456
       
      self.assertRaises(MySpaceError,self.ms.get_activitiesbyappid,person_id,app_id)  
  
  def test_get_activitiesbyappid(self):
      """Tests the calling of get_activitiesbyappid with a valid value of personid
      and appid parameters         
      """
      person_id = "@me"
      app_id = self.appid       
      result = self.ms.get_activitiesbyappid(person_id,app_id)
      self.assertTrue(len(result)>=0)
     

#def get_friendactivitiesv9(self,person_id, fields=None):
 

  def test_get_friend_activities(self):
      """Tests the calling of get_friends_activities with an invalid value of personid,
      parameter         
      """
      person_id = self.ms.get_userid()
      result = self.ms.get_friends_activities(person_id)
      self.assertTrue(len(result)>=0) 
       
#def get_friendactivitiesbyappidv9(self, person_id, app_id, fields=None):
  def test_get_friendactivitiesbyappid_wp(self):
      """Tests the calling of get_friendactivitiesbyappidvwith an invalid value of personid,
      and appid parameters         
      """
      person_id = 123456
      app_id=123456      
      self.assertRaises(MySpaceError,self.ms.get_friendactivitiesbyappid,person_id,app_id)  
     
  def test_get_friendactivitiesbyappid(self):
      """Tests the calling of get_friendactivitiesbyappidvwith an invalid value of personid,
      and appid parameters         
      """
      person_id = "@me"
      app_id = self.appid       
      result = self.ms.get_friendactivitiesbyappid(person_id,app_id)
      self.assertTrue(len(result)>=0)  
     
##def create_activity9(self, title,nobody,templateid,templateparams):


#def get_appdatav9(self, person_id,app_id , fields=None):
  def test_get_appdata_wp(self):
      """Tests the calling of get_appdata with an invalid value of personid,
      and appid parameter         
      """
      person_id = 123456
      app_id = 123456      
      self.assertRaises(MySpaceError,self.ms.get_appdata,person_id,app_id)  

  def test_get_appdata(self):
      """Tests the calling of get_appdata with an invalid value of personid,
      and appid parameter         
      """
      person_id = "@me"
      app_id = self.appid    
      result = self.ms.get_appdata(person_id,app_id)
      self.assertTrue(len(result)>=0)  
       

#def add_appdatav9(self, person_id, app_id, key, value):
  def test_add_appdata(self):
      """Tests the calling of add_appdata with valid parameters   
      """         
      
      app_id = self.appid
      #statuslink = self.ms.add_appdata(person_id, app_id, key='test', value='test value')
      statuslink = self.ms.add_appdata(person_id="@me",app_id=app_id,key='TESTTT',value='testing')  
      self.failIfEqual(None,statuslink,"Error")
 


#def update_appdatav9(self, person_id, app_id, key, value):


#def delete_appdatav9(self, person_id,app_id, fields):


#def get_groupfieldsv9(self):
  def test_get_groupfields(self):
      """Tests the calling of get_groupfields       
      """         
      result = self.ms.get_groupfields()
      self.assertTrue(len(result)>0)


#def get_groupsv9(self,person_id, startindex=None, count=None):
  def test_get_groups(self):
      """Tests the calling of get_groups with an invalid value of personid,
      parameter         
      """
      person_id = "@me"          
      result = self.ms.get_groups(person_id)
      self.assertTrue(len(result)>=0)    
     

#def get_peoplefieldsv9(self):
  def get_peoplefields(self):
      """Tests the calling of get_peoplefields       
      """         
      result = self.ms.get_peoplefields()
      self.assertTrue(len(result)>0)


#def get_peoplesv9(self,person_id, fields=None, filterby=None, filterop=None, filtervalue=None,
#                     format=None, startindex=None, count=None):
  def test_get_person(self):
      """Tests the calling of get_person with a valid value of personid,
      parameter         
      """
      person_id = "@me"          
      result = self.ms.get_person(person_id)
      self.assertTrue(len(result)>=0)   
     

#def get_peoplefriendsv9(self, person_id, fields=None, filterby=None, filterop=None, filtervalue=None,
 #                    format=None, startindex=None, count=None):
  def test_get_friends(self):
      """Tests the calling of get_friends with a valid value of personid,
      parameter         
      """
      person_id = "@me"          
      result = self.ms.get_friends(person_id)
      self.assertTrue(len(result)>=0) 
     
 
    #def get_peoplebyfriendidv9(self,person_id, friend_id, fields=None):
  def test_get_peoplebyfriendid(self):
      """Tests the calling of get_peoplebyfriendid with a valid value of personid,
      parameter         
      """
      person_id = "@me"   
      friends = self.ms.get_friends(person_id)
      friend_id =  friends["entry"][0]["person"]["id"]
      result = self.ms.get_peoplebyfriendid(person_id,friend_id)
      self.assertTrue(len(result)>=0)  
     
    
#def get_supportedsmoodsv9(self,person_id):     
  def test_get_supportedsmoods(self):
      """Tests the calling of get_supportedsmoods with a valid value of personid,
      parameter         
      """
      person_id = "@me"       
      result = self.ms.get_supportedsmoods(person_id)
      self.assertTrue(len(result)>=0)   
    
#def get_supportedsmoodbyidv9(self,person_id, mood_id):
  def test_get_supportedsmoodbyid(self):
      """Tests the calling of get_supportedsmoodbyid with a valid value of personid,
      parameter         
      """
      person_id = "@me"
      mood = self.ms.get_supportedsmoods(person_id)
      mood_id = mood[0]["moodId"]      
      result = self.ms.get_supportedsmoodbyid(person_id,mood_id)      
      self.assertTrue(len(result)>=0) 
    
#def get_statusmoodv9(self,person_id):  
  def test_get_statusmood(self):
      """Tests the calling of get_statusmood with a valid value of personid,
      parameter         
      """
      person_id = "@me"     
      result = self.ms.get_statusmood(person_id)
      self.assertTrue(len(result)>=0) 
    
#def get_friendstatusmoodv9(self, person_id, filterby=None, filterop=None, filtervalue=None, includeself=None,
 #                             culture=None, fields=None):    
 
  def test_get_friendstatusmood(self):
      """Tests the calling of get_friendstatusmood with a valid value of personid,
      parameter         
      """
      person_id = "@me"     
      result = self.ms.get_friendstatusmood(person_id)
      self.assertTrue(len(result)>=0)      
    
#def get_selfstatusmoodhistoryv9(self,person_id, fields=None):
  def test_get_selfstatusmoodhistory(self):
      """Tests the calling of get_selfstatusmoodhistory with a valid value of personid,
      parameter         
      """
      person_id = "@me"     
      result = self.ms.get_selfstatusmoodhistory(person_id)      
      self.assertTrue(len(result)>=0)   
    
#def get_friendstatusmoodhistoryv9(self,person_id, filterby=None, filterop=None, filtervalue=None, includeself=None,
 #                             culture=None, fields=None, startIndex=None, itemsPerPage=None):
  def test_get_friendstatusmoodhistory(self):
      """Tests the calling of get_friendstatusmoodhistory with a valid value of personid,
      parameter         
      """
      person_id = "@me"     
      result = self.ms.get_friendstatusmoodhistory(person_id)
      self.assertTrue(len(result)>=0)          
    
#def get_statusmoodbyfriendidv9(self,person_id, friend_id, filterby=None, filterop=None, filtervalue=None, includeself=None,
  #                            culture=None, fields=None, startIndex=None, itemsPerPage=None):
  def test_get_statusmoodbyfriendid(self):
      """Tests the calling of get_statusmoodbyfriendid with a valid value of personid,
      parameter         
      """
      person_id = "@me"   
      friends = self.ms.get_friends(person_id)
      friend_id =  friends["entry"][0]["person"]["id"]
      result = self.ms.get_statusmoodbyfriendid(person_id,friend_id)
      self.assertTrue(len(result)>=0)  
               
    

#def get_statusmoodhistorybyfriendidv9(self,person_id, friend_id, filterby=None, filterop=None, filtervalue=None, includeself=None,
#                              culture=None, fields=None, startIndex=None, itemsPerPage=None):
  def test_get_statusmoodhistorybyfriendid(self):
      """Tests the calling of get_statusmoodhistorybyfriendid with a valid value of personid,
      parameter         
      """
      person_id = "@me"   
      friends = self.ms.get_friends(person_id)
      friend_id =  friends["entry"][0]["person"]["id"]
      result = self.ms.get_statusmoodhistorybyfriendid(person_id,friend_id)      
      self.assertTrue(len(result)>=0)           
    
#def set_statusv9(self,person_id, latitude=None, longitude=None, moodname=None, status=None):
  def test_set_status(self):
      """Tests the calling of set_status with a valid value of personid,
      parameter         
      """
      person_id = "@me"     
      statuslink = self.ms.set_status(person_id,latitude='40',longitude='122',moodname='excited',status='testing')
      self.assertTrue(len(statuslink)>=0)  
    
#def get_statusmoodcommentsv9(self,person_id):     
  #def test_get_statusmoodcomments(self):
      """Tests the calling of get_statusmoodhistorybyfriendid with a valid value of personid,
      parameter         
      """
      #person_id = "@me"        
      #result = self.ms.get_statusmoodcomments(person_id)
      #self.assertTrue(len(result)>=0)    
        
    
#def set_statusmoodcommentsv9(self,person_id, body, statusid):
  #def test_set_statusmoodcomments(self,person_id, body, statusid):
      """Tests the calling of set_statusmoodcomments with a valid value of personid,
      parameter         
      """
      #person_id = "@me"     
      #bodyparam = '{"body":"this is a comment about your status"}'
      #status_id = self.ms.get_statusmood(person_id)
      #print status_id
      #statuslink = self.ms.set_statusmoodcomments(person_id,body,status_id)
      #self.assertTrue(len(statuslink)>=0)  

#def send_notificationv9(self,person_id, recipientids, templateparams, mediaitems):
  def test_send_notification(self):
      """Tests the calling of send_notification with a valid parameters         
      """
      person_id = self.ms.get_userid()
      #friends = self.ms.get_friends(person_id)
      #friend_id =  friends["entry"][0]["person"]["id"]
      #recipientids = friend_id
      templateparam ='[{"key":"content","value":"Test notification content from python sdk"},\
                                {"key":"button0_surface","value":"canvas"},\
                                {"key":"button0_label","value":"Go To App Canvas"},\
                                {"key":"button1_label","value":"Go To App Profile"}]'
      statuslink = self.ms.send_notification(person_id=person_id, recipientids="333220680", templateparams=templateparam, mediaitems='http://opensocial.myspace.com/roa/09/mediaitemcomments/333220680/@self')
            
      self.assertTrue(len(statuslink)>=0) 

 #def add_subscription(self, type, endpoint, query, metadata, batchsize, rate, format, addlist, removelist):
  def test_add_subscription(self):
      """Tests the calling of add_subscription with a valid parameters         
      """      
      # make sure you specify unique value for end point each time
      statuslink = self.ms.add_subscription(type='All',
                                             endpoint='http://myspace.si-sv2826.com/myposthandler17.ashx',
                                          query='{}',metadata='',batchsize='1000',  
                                             rate= '100',format='application/atom+xml', addlist='[ ]',removelist='[ ]')

      self.assertTrue(len(statuslink)>=0) 

#def update_subscription(self, subcriptionid, type, endpoint, query, metadata, batchsize, rate, format, addlist, removelist):
 # def test_update_subscription(self):
#      """Tests the calling of update_subscription with a valid parameters         
      """      
      subscription = self.ms.get_allsubscription()
      
      statuslink = self.ms.update_subscription(subcriptionid='2803',type='ApplicationUsers',
                                             endpoint='http://myspace.si-sv3063.com/myposthandler4.ashx',
                                           query='{}',metadata='UserInfo,UserSubscribers,ApplicationData',batchsize='1000',  
                                             rate= '100',format='application/atom+xml', addlist='[ ]',removelist='[ ]')
      self.assertTrue(len(statuslink)>=0)""" 


   
   

#def delete_subscription(self, subscription_id):   
# def update_subscription(self):
      """Tests the calling of update_subscription with a valid parameters         
      """      
 #     statuslink = self.ms.update_subscription(subcriptionid='2803',type='ApplicationUsers',
  #                                           endpoint='http://myspace.si-sv3063.com/myposthandler4.ashx',
   #                                        query='{}',metadata='UserInfo,UserSubscribers,ApplicationData',batchsize='1000',  
    #                                         rate= '100',format='application/atom+xml', addlist='[ ]',removelist='[ ]')
     # self.assertTrue(len(statuslink)>=0) 

#def get_subscription(self, subscription_id):
  def test_get_allsubscription(self):
      """Tests the calling of get_allsubscription with a valid parameters         
      """      
      statuslink = self.ms.get_allsubscription()
      self.assertTrue(len(statuslink)>=0) 
    

#def search_people(self, searchTerms, format=None, count=None,
 #                  startPage=None, searchBy=None, gender=None,
  #                 hasPhoto=None, minAge=None, maxAge=None,
   #                location=None , distance=None, latitude=None,
    #               culture=None, countryCode=None):
    
  def test_search_people(self):
      """Tests the calling of search_people with a valid parameters         
      """      
      result = self.ms.search_people(searchTerms='unit test')
      self.assertTrue(len(result)>=0) 

#def search_images(self, searchTerms, format=None, count=None,
 #                  startPage=None, culture=None, sortBy=None, sortOrder=None):
  def test_search_images(self):
      """Tests the calling of search_images with a valid parameters         
      """      
      result = self.ms.search_images(searchTerms='unit test')
      self.assertTrue(len(result)>=0) 

   # def search_videos(self, searchTerms, format=None, count=None,
   #                  startPage=None, culture=None, tag=None, videoMode=None):
  def test_search_videos(self):
      """Tests the calling of search_videos with a valid parameters         
      """      
      result = self.ms.search_videos(searchTerms='unit test')
      self.assertTrue(len(result)>=0) 
 

#def get_personpoco(self,person_id, page=None, page_size=None, fields=None):
  def test_get_personpoco(self):
      """Tests the calling of get_personpoco with a valid parameters         
      """      
      user_id = self.ms.get_userid()
      result = self.ms.get_personpoco(user_id)
      self.assertTrue(len(result)>=0) 

#def get_friendspoco(self,person_id, page=None, page_size=None):
  def test_get_friendspoco(self):
      """Tests the calling of get_friendspoco with a valid parameters         
      """      
      user_id = self.ms.get_userid()
      result = self.ms.get_friendspoco(user_id)
      self.assertTrue(len(result)>=0) 

  #def get_profilecommentsv9(self,person_id, fields=None):
  def test_get_profilecomments(self):
      """Tests the calling of get_profilecomments with an invalid value for the personid parameter         
      """
      person_id = 123456      
      self.assertRaises(MySpaceError,self.ms.get_profilecomments,person_id)


  def test_get_profilecomments(self):
      """Tests the calling of get_profilecomments with a valid value for the personid parameter         
      """
      person_id = "@me"
      resp = self.ms.get_profilecomments(person_id)    
      
  
        
  
      
      



  