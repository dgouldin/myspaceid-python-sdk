
#subscription
API_STREAM_SUBSCRIPTION = 'http://api.myspace.com/stream/subscription/%s'

class RealStream():
    def __init__(self,objmyspacecontext):
        global context
        context= objmyspacecontext    
        
    """ Real Time Stream
        Resource:     http://api.myspace.com/stream/subscription? 
        Description: Add Subscription
        Subscription Usage : addSubscriptionV9('All','http://myspace.mycompany.com/handler.ashx','{}','',1,1);                                  
        Details:    http://wiki.developer.myspace.com/index.php?title=Category:Real_Time_Stream
    """       
    def add_subscription(self, type, endpoint, query, metadata, batchsize, rate, format, addlist, removelist):
    #def create_subscription(self):              
                
        bodytext = '{"Subscription" : {\
                   "Type" :"' + type + '",\
                   "Endpoint" : "' + endpoint + '",\
                   "Query" :' + query + ' ,\
                 "MetaData" : "' + metadata + '",\
                   "BatchSize" : ' + batchsize + ',\
                   "Rate" :' + rate + ',\
                   "Format" : "' + format + '",\
                   "UserList" : {\
                    "AddList" : ' + addlist + ',\
                    "RemoveList" :' + removelist + '}}}' 
                    
        #bodytext = '{"Subscription" : {"Type" : "ApplicationUsers","Endpoint" : "http://myspace.si-sv3063.com/myposthandler1.ashx","Query" : {},"MetaData" : "UserInfo,UserSubscribers,ApplicationData","BatchSize" : 1000,"Rate" : 100,"Format" : "application/atom+xml","UserList" : {"AddList" : [],    "RemoveList" : []}}}'         
        subscription_create_url = API_STREAM_SUBSCRIPTION % ''
        #subscription_create_url = 'http://api.myspace.com/stream/subscription'       
        params = {}
      
        return context.callmyspaceapi(subscription_create_url, method='POST', parameters=params, body=bodytext) 
       

    """ Real Time Stream
        Resource:     http://api.myspace.com/stream/subscription/{subscriptionId}? 
        Description: Update subscription
        Update Subscription Usage : updateSubscriptionV9('1234', 'All','http://myspace.mycompany.com/handler.ashx','{}','',1,1);                                  
        Details:    http://wiki.developer.myspace.com/index.php?title=Category:Real_Time_Stream
    """ 
    def update_subscription(self, subcriptionid, type, endpoint, query, metadata, batchsize, rate, format, addlist, removelist):   
#    def update_subscription(self,subscription_id):
        
                   
        bodytext = '{"Subscription" : {\
                   "id" :' + subcriptionid + ',\
                   "Type" :"' + type + '",\
                   "Endpoint" : "' + endpoint + '",\
                   "Query" :' + query + ' ,\
                 "MetaData" : "' + metadata + '",\
                   "BatchSize" : ' + batchsize + ',\
                   "Rate" :' + rate + ',\
                   "Format" : "' + format + '",\
                   "UserList" : {\
                    "AddList" : ' + addlist + ',\
                    "RemoveList" :' + removelist + '}}}' 
                    
        #bodytext='{"Subscription" : {"Type" : "ApplicationUsers","Endpoint" : "http://myspace.si-sv3063.com/myposthandler.ashx","Query" :{"Or" : [ {"And" : [ {"Object" : "Audio"},{"Verb" : "Play"},{"UserType" : "Band"}  ]},  {"And" : [ {"EventSource" : "ApplicationId.123456"}, {"Or" : [{"Location" : {"Lat" : 36.1, "Lon" : -115.1, "Radius" : 30}},  {"Location" : {"Lat" : 28.7, "Lon" : -95.3, "Radius" : 1000}} ]}, {"Not" : [ {"Text" : "Michael Jackson"} ]}  ]} ]}, "MetaData" : "UserInfo,UserSubscribers,ApplicationData", "BatchSize" : 1000,  "Rate" : 100, "Format" : "application/atom+xml", "UserList" : { "AddList" : [6221,452341,4322],  "RemoveList" : [63453,142311,896784]  }}}'
        #bodytext='{"Subscription" : {"id" : 2801,"Type" : "ApplicationUsers","Endpoint" : "http://myspace.si-sv3063.com/myposthandler.ashx","Query" :{}, "MetaData" : "UserInfo,UserSubscribers,ApplicationData", "BatchSize" : 1000,  "Rate" : 100, "Format" : "application/atom+xml", "UserList" : { "AddList" : [],  "RemoveList" : []  }}}'
                   
        subscription_update_url = API_STREAM_SUBSCRIPTION % subcriptionid     
        params = {}
            
        return context.callmyspaceapi(subscription_update_url, method='PUT', parameters=params, body=bodytext) 

    """ Real Time Stream
        Resource:      http://api.myspace.com/stream/subscription/{subscriptionId}? 
        Description: Delete Subscription
        Parameter:  subcription_id (mandatory) id of subscrption which user want to delete                                  
        Details:    http://wiki.developer.myspace.com/index.php?title=Category:Real_Time_Stream
    """ 
    def delete_subscription(self, subscription_id):   
        subscription_create_url = API_STREAM_SUBSCRIPTION % subscription_id       
        params = {}
            
        return context.callmyspaceapi(subscription_create_url, method='DELETE', parameters=params) 

       
    """ Real Time Stream
        Resource:      http://api.myspace.com/stream/subscription/{subscriptionId}? 
        Description: Get Subscption 
        Parameter:  subcription_id (mandatory) id of subscrption which user want to Get                                  
        Details:    http://wiki.developer.myspace.com/index.php?title=Category:Real_Time_Stream
    """  
    def get_subscription(self, subscription_id):        
                  
        subscription_url = API_STREAM_SUBSCRIPTION % subscription_id        
        params = {}        
        return context.callmyspaceapi(subscription_url, method='GET', parameters=params)        
           
    

    """ Real Time Stream
        Resource:   http://api.myspace.com/stream/subscription/{all}? 
        Description:Delete all Subscription                                       
        Details:    http://wiki.developer.myspace.com/index.php?title=Category:Real_Time_Stream
    """ 
    def delete_allsubscription(self):   
        subscription_create_url = API_STREAM_SUBSCRIPTION % "@all"       
        params = {}            
        return context.callmyspaceapi(subscription_create_url, method='DELETE', parameters=params) 
       
    """ Real Time Stream
        Resource:   http://api.myspace.com/stream/subscription/{subscriptionId}? 
        Description:Get all Subscption                                         
        Details:    http://wiki.developer.myspace.com/index.php?title=Category:Real_Time_Stream
    """  
    def get_allsubscription(self):        
                  
        subscription_url = API_STREAM_SUBSCRIPTION % "@all"        
        params = {}        
        return context.callmyspaceapi(subscription_url, method='GET', parameters=params)
    
    