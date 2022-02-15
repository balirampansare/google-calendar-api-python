from Google import Create_Service
from pprint import pprint


CLIENT_SECRET_FILE = 'client_secret_file.json' 
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar'] 

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
calendar_id = 'dgn1p9cn2rpltml651ffpbhkgs@group.calendar.google.com'


#events = service.events().list(calendarId = calendar_id).execute()
#pprint(events) # this will give all the events of particular calendar


EventId = 'icd88r65bgm7rrd2iv30qcm2jk'

# First retrieve the event from the API.
event = service.events().get(calendarId=calendar_id, eventId=EventId).execute()

event['summary'] = 'Project Meet'

updated_event = service.events().update(calendarId=calendar_id, eventId=EventId, body=event).execute()
