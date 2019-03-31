#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests


# Function for getting directions names for a given route name

# In[43]:


def printDirectionName(route_name,api_key) :
    
    stop_numbers_URL = "http://realtime.mbta.com/developer/api/v2/stopsbyroute?"       + "api_key=" + api_key      + '&route=' + route_name     + '&format=json'
    
    print(stop_numbers_URL)  
    
    response =requests.get(stop_numbers_URL)
    data =  response.json();
    direc1 = data['direction'][0]['direction_name']
    cnt = 0
    for i in data['direction']:
        print(cnt,':',i['direction_name'])
        cnt = cnt + 1
        print()
        
api_key = 'wX9NwuHnZU2ToO7GmGR9uw'
#Route names: Red, Orange, Blue, Green-B, Green-C, Green-D, Green-E
route_name = 'Blue'
printDirectionName(route_name,api_key)


# Function for getting route number for a given route name, direction, and number of stops starting at that direction

# In[41]:


def getRouteNum(route_name,direction,stops_from_direc,api_key) :

    URL = "http://realtime.mbta.com/developer/api/v2/stopsbyroute?"       + "api_key=" + api_key      + "&route=" + route_name     + "&format=json"
    
    print(URL)
    response =requests.get(URL)
    data =  response.json();
    
    # data['direction'][0]['stop'][1] gives westbound data for Revere 
    return(data['direction'][direction]['stop'][stops_from_direc]['stop_id'])


api_key = 'wX9NwuHnZU2ToO7GmGR9uw'
route_name = 'Blue'
direction = 0
stops_from_direc = 1 # Number of stops after direction
stop_id = getRouteNum(route_name,direction,stops_from_direc,api_key)
print(stop_id)


# In[44]:


import requests
import json
import datetime

#Roxbury Crossing stop IDs: 70008 -> Forest Hills, 70009 -> Oak Grove
# Revere beach = 70057

route_name = 'Blue'
api_key = 'b17a6776b76b49a0b0dc37fbe78ce649'

requestURL = "https://api-v3.mbta.com/predictions?"      + "filter[stop]=70057"     + "&filter[route]=" + route_name     + "&include=stop,route,trip,facility"     + "&api_key=" + api_key
print(requestURL)

response = requests.get(requestURL)

if response.status_code == 200:
    print("\nRequest was processed successfully\n")
else:
    print('\nRequest was not processed successfully\n')

data = response.json()['data']
#print(data)
        
def mbtaTimeToDatetime(inputTime) :
    inputTime = inputTime[0:19]
    return datetime.datetime.strptime(inputTime, '%Y-%m-%dT%H:%M:%S')

#Returns array of 4 integers: [closest minutes, closest seconds, 2nd closest minutes, 2nd closest seconds]
# Sometimes this will incorrectly return an extremely large numbers
def nextTrain(requestURL):
    data = requests.get(requestURL).json()['data']
    ETA1 = mbtaTimeToDatetime(data[0]['attributes']['arrival_time']) - datetime.datetime.now()
    ETA2 = mbtaTimeToDatetime(data[1]['attributes']['arrival_time']) - datetime.datetime.now()
    return [int(ETA1.seconds / 60), ETA1.seconds % 60, int(ETA2.seconds / 60), ETA2.seconds % 60]

next2trains = nextTrain(requestURL)
print('Train 1 time:', next2trains[0],':',next2trains[1])
print('Train 2 time:',next2trains[2],':',next2trains[3])


# In[ ]:




