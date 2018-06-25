#!/usr/bin/env python3
# Author; Liam Easton
# Script; Bacon API Caller

import urllib.parse
import urllib.request

def get_bacon():
    api_url = ("https://baconipsum.com/api/?")
    values  = {'type' : 'meat-and-filler','paras' : '3','format' : 'text'}
    
    #encode values to be passed as CGI
    encoded_values = urllib.parse.urlencode(values)
    
    #combine url with values
    combined_url = (api_url) + (encoded_values)
    #send out request, grab response and decode to utf-8
    request = urllib.request.Request(combined_url)
    response = urllib.request.urlopen(request)
    response_data = response.read().decode('utf-8')
    #print bacon ipsum
    print(response_data) 

def main():
    get_bacon()

if __name__ == '__main__':
    #Run when started from the command line
    main()

