from time import strftime
from Google import Create_Service
from datetime import datetime,timedelta
CLIENT_SECRET_FILE = 'client_secret_file.json' 
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar'] 

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

#----------Creating Calendar----------------#

request_body = {
    'summary': 'Project Track', 
    'timeZone': 'Asia/Kolkata'
}
response = service.calendars().insert(body=request_body).execute()
calendar_id = response['id']

start_time = datetime(2022,2,15,13,30,0) #(yyyy,mm,dd,hr,min,sec)
end_time = start_time + timedelta(hours = 2)
timeZone = 'Asia/Kolkata'
#----------request body of event-----------#


event_request_body = {
    'start':{
        'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone' : timeZone,
    },

    'end':{
        'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone' : timeZone
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
    calendarId = calendar_id,
    maxAttendees =maxAttendees,
    sendNotifications=sendNotification,
    sendUpdates=sendUpdates,
    body=event_request_body,
).execute()
