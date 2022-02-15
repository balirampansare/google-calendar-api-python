#importing Create_Service function from google module
from Google import Create_Service

#creating a variables to store info required to create google calendar api service

CLIENT_SECRET_FILE = 'client_secret_file.json' 
API_NAME = 'calendar'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/calendar'] 

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

#before execution make sure that your app is in production state form oauth console screen
#on executing it will create token file, which basically store our authentication details
#authentication process takes place for first execution only :)

#----------Creating Calendar----------------#

request_body = {
    'summary': 'DailyTask', 
    'timeZone': 'Asia/Kolkata'
}
response = service.calendars().insert(body=request_body).execute()

