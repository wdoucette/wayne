import googleapiclient.discovery
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

SERVICE_ACCOUNT_FILE="cred.json"

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
credentials = credentials.with_subject('email-stuff@optimal-transit-851.iam.gserviceaccount.com')
gmail = googleapiclient.discovery.build('gmail', 'v1', credentials=credentials)

watchRequest = {
    'labelIds' : ['INBOX'],
    'topicName' : 'projects/optimal-transit-851/topics/MyTopic'
}

userId="doucette.wayne"


message = gmail.users().drafts().list(userId=userId).execute() #getProfile(userId=userId).execute() #gmail.users().messages().get(userId=user_id, id=msg_id).execute()

print message
#print 'Message snippet: %s' % message['snippet']


#gmail.users().watch(userId='doucette.wayne', body=watchRequest).execute()
