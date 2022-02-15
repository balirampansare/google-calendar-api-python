from Google import Create_Service, convert_to_RFC_datetime 

CLIENT_SECRET_FILE = 'client_secret_file.json' 
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar'] 

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

calendar_id = 'dgn1p9cn2rpltml651ffpbhkgs@group.calendar.google.com'
EventId = 'icd88r65bgm7rrd2iv30qcm2jk'

service.events().delete(calendarId=calendar_id, eventId=EventId).execute()