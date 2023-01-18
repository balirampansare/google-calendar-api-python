<h1 align="center">Google Calendar API Using Python</h1>
<p align="center">
<img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />
<img src="https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white" />
</p>

Want to integrate google calendar api in your application? [Link](https://developers.google.com/calendar/api)

At the end you will know how to create, update, delete the calendars and events.

## Prerequisites [[link](https://developers.google.com/calendar/api/quickstart/python)]
- Create Google Cloud Platform project with the google calendar API enabled and download the client json file by creating OAuth Credentials. ([googleconsolecloudlink](https://console.cloud.google.com))
- Save the client json file in your working directory.
- A Google account with Google Calendar enabled.

## Step 1: Install the Google client library
 ```
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  ```
## Step 2: Configure the sample 
- In your working directory, create a file name google.py  file.
- To include code in it check out the repo above or the link ([configure the sample](https://developers.google.com/calendar/api/quickstart/python))

## Step 3: Creating service to create google calendar api
- While creating service you need to add scope.
- scope - Access that should be given to the user ([link](https://developers.google.com/calendar/api/guides/auth))
- In our project we are giving read, write action to the user

## Step 4: Create,Update,Delete Calendar
Create the Calendar ([Create](https://developers.google.com/calendar/api/v3/reference/calendars/insert))
```
#Supplying the required calendar info in request_body

request_body = {
    'summary': 'calendarSummary', #Calendar Title
    'timeZone': 'Asia/Kolkata'
}

#returning the request_body in response
response = service.calendars().insert(body=request_body).execute()
```

Update the Calendar ([Update](https://developers.google.com/calendar/api/v3/reference/calendars/update))

```
#retrieve the calendar you want to update
# here i retrieved the required calendar as myCalendar

myCalendar['summary'] = 'new summary'
myCalendar['description'] = 'new description'

service.calendars().update(calendarId = myCalendar['id'],body =myCalendar).execute()

#check out calendar_update.py file for better explanation.
```

Delete the Calendar ([Delete](https://developers.google.com/calendar/api/v3/reference/calendars/delete))

```
service.calendars().delete(calendarId='id_of_calendar_to_delete').execute()
```

## Step 5: Create, Update, Delete Event

Create Event

Below is the code of the project, you can add more body request for event. [Create event](https://developers.google.com/calendar/api/v3/reference/events/insert)
```
#id of the project
calendar_id_proj = '...'

#----------request body of event-----------#


event_request_body = {
    'start':{
        'dateTime': convert_to_RFC_datetime(2022,2,13,2 ),  #(yyyy,mm,dd,time)
        'timeZone' : 'Asia/Kolkata'
    },

    'end':{
        'dateTime': convert_to_RFC_datetime(2022,2,13,3),  
        'timeZone' : 'Asia/Kolkata'
    },

    'summary': 'MLProj Meet',
    'description':'discussion of the final yr project',
    'colorId': 5,
    'Status': 'confirmed',
    'transparency':'opaque',
    'visibility':'private',
    'location':'Thane, Viviana',
    'attendees':[
        {
            'displayName' : 'Tom',
            'comment' : 'cool guy',
            'email' : 'tp@example.com',
            'optional': False, #optional: means whether this attendee is optional or not
            'organizer': True,
            'responseStatus': 'accepted'
        }
    ]

}

maxAttendees = 5
sendNotification = True
sendUpdates = 'none'

#-----------Creating Event------------#

response = service.events().insert(    
    calendarId = calendar_id_proj,
    maxAttendees =maxAttendees,
    sendNotifications=sendNotification,
    sendUpdates=sendUpdates,
    body=event_request_body,
).execute()
```

Update Event ([Link](https://developers.google.com/calendar/api/v3/reference/events/update))

```
calendar_id = '...'
eventId = '...'
# First retrieve the event from the API.
event = service.events().get(calendarId=calendar_id, eventId=EventId).execute()

event['summary'] = 'Project Meet'
.
.

updated_event = service.events().update(calendarId=calendar_id, eventId=EventId, body=event).execute()

```

Delete Event ([Link](https://developers.google.com/calendar/api/v3/reference/events/delete))

```
calendar_id = '...'
EventId = '...'

service.events().delete(calendarId=calendar_id, eventId=EventId).execute()
```



