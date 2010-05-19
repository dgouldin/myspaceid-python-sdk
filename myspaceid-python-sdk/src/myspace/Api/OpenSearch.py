
API_PEOPLESEARCH_URL = 'http://api.myspace.com/opensearch/people'
API_IMAGESEARCH_URL = 'http://api.myspace.com/opensearch/images'
API_VIDEOSEARCH_URL = 'http://api.myspace.com/opensearch/videos'

class OpenSearch():
    
    def __init__(self,objmyspacecontext):
        global context
        context= objmyspacecontext
    
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
        
        # validate common parameters
        context.validate_params(locals())
        
        
        #validate the format param - it can be one of 'json', or 'xml'
        #valid_format_values = ['json', 'xml']
        #if fromat is not None:
        #   if fromat not in valid_format_values:
        #        raise MySpaceError('Invalid Parameter Value. Format must be one of %s' % str(valid_format_values))
        #       return
                
        search_request_url = API_PEOPLESEARCH_URL   
        #set up extra params, if any
        params = {}
        if format is not None:
            params['format'] = format
        if count is not None:
            params['count'] = count
        if startPage is not None:
            params['startPage'] = startPage
        if searchBy is not None:
            params['searchBy'] = searchBy
        if gender is not None:
            params['gender'] = gender
        if hasPhoto is not None:
            params['hasPhoto'] = hasPhoto
        if minAge is not None:
            params['minAge'] = minAge
        if maxAge is not None:
            params['maxAge'] = maxAge
        if location is not None:
            params['location'] = location
        if distance is not None:
            params['distance'] = distance
        if latitude is not None:
            params['latitude'] = latitude
        if culture is not None:
            params['culture'] = culture
        if countryCode is not None:
            params['countryCode'] = countryCode        
        if searchTerms is not None:
            params['searchTerms'] = searchTerms
          
        return context.callmyspaceapi(search_request_url, parameters=params)
    
      
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
        # validate common parameters
        context.validate_params(locals())
        
        #validate the format param - it can be one of 'json', or 'xml'
        #valid_format_values = ['json', 'xml']
        #if fromat is not None:
        #   if fromat not in valid_format_values:
        #        raise MySpaceError('Invalid Parameter Value. Format must be one of %s' % str(valid_format_values))
        #       return
                
        imagesearch_request_url = API_IMAGESEARCH_URL   
        
        #set up extra params, if any
        params = {}
        if format is not None:
            params['format'] = format
        if count is not None:
            params['count'] = count
        if startPage is not None:
            params['startPage'] = startPage
        if culture is not None:
            params['culture'] = culture
        if sortBy is not None:
            params['sortBy'] = sortBy
        if sortOrder is not None:
            params['sortOrder'] = sortOrder
        if searchTerms is not None:
            params['searchTerms'] = searchTerms
        
        return context.callmyspaceapi(imagesearch_request_url, parameters=params)
    
    
       
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
        # validate common parameters
        context.validate_params(locals())
        
        #validate the format param - it can be one of 'json', or 'xml'
        #valid_format_values = ['json', 'xml']
        #if fromat is not None:
        #   if fromat not in valid_format_values:
        #        raise MySpaceError('Invalid Parameter Value. Format must be one of %s' % str(valid_format_values))
        #       return
                
        videosearch_request_url = API_VIDEOSEARCH_URL   
        
        #set up extra params, if any
        params = {}
        if format is not None:
            params['format'] = format
        if count is not None:
            params['count'] = count
        if startPage is not None:
            params['startPage'] = startPage
        if culture is not None:
            params['culture'] = culture
        if tag is not None:
            params['tag'] = tag
        if videoMode is not None:
            params['videoMode'] = videoMode
        if searchTerms is not None:
            params['searchTerms'] = searchTerms
        
        return context.callmyspaceapi(videosearch_request_url, parameters=params)
    
