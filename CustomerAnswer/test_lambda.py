import sys
sys.path.insert(0, "./lib")
import nexmo
application_id= "d402c845-53f6-4ca1-b8d6-7d44bad1ceec"
private_key= './nexmo.key'

def handler(event, context):
  client = nexmo.Client(application_id=application_id, private_key=private_key)
  response = client.create_call({ 
    "to": [{
        'type':'phone', 
        'number': '17863856106'
        }], 
    'from': { 
        'type': 'phone', 
        'number': '17863856106'
        }, 
    'answer_url': [ "https://nv8gy023v7.execute-api.us-east-1.amazonaws.com/dev/answer-agent" ], 
    'event_url': [ "https://nv8gy023v7.execute-api.us-east-1.amazonaws.com/dev/event-agent" ]
  })

