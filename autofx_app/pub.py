from google.cloud import pubsub_v1
import datetime

#import googleapiclient.gmail
#request = {
#  'labelIds': ['INBOX'],
#  'topicName': 'projects/myproject/topics/mytopic'
#}
#gmail.users().watch(userId='me', body=request).execute()


project_id = "optimal-transit-851"
topic_name = "MyTopic"

publisher = pubsub_v1.PublisherClient()
# The `topic_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/topics/{topic_name}`
topic_path = publisher.topic_path(project_id, topic_name)

for n in range(1, 10):
    data = u'Message number {}'.format(n)
    # Data must be a bytestring
    print "n:" + str(n)
    data = data.encode('utf-8')
    
    # When you publish a message, the client returns a future.
    future = publisher.publish(topic_path, data=data, time=str(datetime.datetime.now()))
    print(future.result())

print('Published messages.')
