from Google import Create_Service


CLIENT_SECRET_FILE = 'client_secret_file.json' 
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar'] 

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

#retrieving all the calendar list
response = service.calendarList().list().execute()

#retrieving all calendar list resources
calendarItems = response.get('items')

myCalendar = filter(lambda x: 'DailyTask' in x['summary'],calendarItems) 
myCalendar = next(myCalendar) 


myCalendar['summary'] = 'Daily Task'
myCalendar['description'] = 'Task need to be done'

service.calendars().update(calendarId = myCalendar['id'],body =myCalendar).execute()