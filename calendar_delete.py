from Google import Create_Service
from pprint import pprint

CLIENT_SECRET_FILE = 'client_secret_file.json' 
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar'] 

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

service.calendars().delete(calendarId='rrtb7o5atcrpn86s1p78gdjn8c@group.calendar.google.com').execute()