import sys
import os
import boto3
import re
sys.path.insert(0, "./lib")
from pypodio2 import api
import nexmo
application_id = os.environ['nexmoappid']
private_key = '\n'.join(os.environ['nexmokey'].split('\\n'))
import json

def handler(event, context):

    print sys._getframe().f_code.co_name + " " + json.dumps(event)
    response = {}
    try:
        qs = event['context']['resource-path'].split('/')
        action = qs[1]
        direction = qs[2]

        response = {
            'inbound': handle_inbound,
            'outbound': handle_outbound
        }[direction](event, action)

    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0]),
            "event": event
        }
    finally:
        print json.dumps(response)
        return response

def handle_inbound(body, t=None):
    try:
        print sys._getframe().f_code.co_name
        if t == 'answer':
            response = inbound_answer()
        elif t == 'event':
            event = body['body-json']
            if 'dtmf' in event:
                response = inbound_dtmf(event)
            else:
                db = boto3.resource('dynamodb', region_name='us-east-1')
                response = {
                    'ringing': inbound_ringing,
                    'started': inbound_started,
                    'answered': inbound_answered,
                    'completed': inbound_completed,
                }[event['status']](event, db)
            response = {}
        else:
            raise KeyError("action={}".format(t))
    except Exception as e:
        response = { "error": "Error in parameter {}".format(e.args[0]) }
    finally:
        return response

def inbound_answer():
    try:
        print sys._getframe().f_code.co_name
        response = [
            { 
                "action": "stream",
                "streamUrl": [ os.environ['silence1s'] ]
            },
            {
                "action": "talk",
                "text": os.environ['welcome']
            },
            {
                "action": "conversation",
                "name": "samana-support",
                "startOnEnter": "false",
                "musicOnHoldUrl": [os.environ['moh']]
            }
        ]
    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "OS variable {} not set".format(e.args[0])
        }
    finally:
        return response

def inbound_ringing(event, db):
    print sys._getframe().f_code.co_name + " " + json.dumps(event)
    return {}

def inbound_started(event, db):
    print sys._getframe().f_code.co_name + " " + json.dumps(event)
    return {}

def inbound_answered(event, db):
    try:
        print sys._getframe().f_code.co_name + " " + json.dumps(event)
        table = db.Table("SamanaNexmo")
        db.Table("SamanaNexmo").put_item(Item={
            "uuid": event['uuid'],
            "direction": event['direction'],
            "conversation_uuid": event['conversation_uuid'],
            "answered": False,
            "to": event['to'],
            "from": event['from'],
            "status": 'waiting',
            "answered": False
        });
        response = {}
    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0])
        }
    except Exception as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": e.args[0],
            "errortype": str(type(e)),
        }
    finally:
        
        return call_agent(event, { "uuid": event['uuid'] }, db)

def inbound_completed(event, db):
    try:
        print sys._getframe().f_code.co_name + " " + json.dumps(event)
        table = db.Table("SamanaNexmo")
        table.update_item(
            Key={ "uuid": event['uuid'] },
            UpdateExpression="set #d = :duration, start_time = :st, end_time = :et, rate = :r, price = :p, #s = :s",
            ExpressionAttributeValues={ 
                ":duration": event['duration'],
                ":st": event['start_time'],
                ":et": event['end_time'],
                ":r": event['rate'],
                ":p": event['price'],
                ":s": event['status']
            },
            ExpressionAttributeNames= { "#s": "status", "#d": "duration" },
            ReturnValues="UPDATED_NEW")
        response = {}
    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0])
        }
    except Exception as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": e.args[0],
            "errortype": str(type(e)),
        }
    finally:
        return response

def inbound_dtmf(event, db):
    print sys._getframe().f_code.co_name + " " + json.dumps(event)
    return {}

def call_agent(event, caller_data, db):
    table = db.Table("AgentCalls")
    try:
        print sys._getframe().f_code.co_name + " " + json.dumps(event) + " " + json.dumps(caller_data)
        if 'phones' not in caller_data:
            phones = get_phones()
            #phones = [ '17863856106', '12023344433' ]
            print json.dumps(phones)

        ringing_timer = 15

        if len(phones) < 1: raise Exception
        print "starting communication with nexmo"
        client = nexmo.Client(application_id=application_id, private_key=private_key)
        call_data = { 
            "to": [{
                'type':'phone', 
                'number': re.sub('[^0-9+]', '', phones[0])
                }], 
            'from': { 
                'type': 'phone', 
                'number': '17865903880'
                }, 
            'answer_url': [ "https://9vpr0y3928.execute-api.us-east-1.amazonaws.com/dev/answer/outbound" ], 
            'event_url' : [ "https://9vpr0y3928.execute-api.us-east-1.amazonaws.com/dev/event/outbound" ],
            'ringing_timer': ringing_timer
        }
        print "communication with nexmo established."
        print "starting agent call."
        agent_call_data = client.create_call(call_data)
        print "calling: " + json.dumps(agent_call_data)

        newcall_data = table.put_item(Item={
            "uuid": agent_call_data['uuid'],
            "caller_uuid": caller_data['uuid'],
            "direction": agent_call_data['direction'],
            "conversation_uuid": agent_call_data['conversation_uuid'],
            "status": agent_call_data['status'],
            "phones": phones
        });
        print "newcall_data: " + json.dumps(newcall_data)
        response = {}
    except KeyError as e:
        print "keyerror: " + json.dumps(e.args)
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0])
        }
    except Exception as e:
        print "Exception: " + json.dumps(e.args)
        table.update_item(
            Key                      = { "uuid": event['uuid'] },
            UpdateExpression         = "set #p = :p",
            ExpressionAttributeValues={ 
                ":p": "Unknown Error"
                },
            ExpressionAttributeNames = { 
                "#p": "agent_phones"
                },
            ReturnValues="UPDATED_NEW")
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": e.args[0],
            "errortype": str(type(e)),
        }
    except:
        print "Unknown error"
        exit(1)
    finally:
        return response

def handle_outbound(body, t=None):
    try:
        print sys._getframe().f_code.co_name
        db = boto3.resource('dynamodb', region_name='us-east-1')

        if t == 'answer':
            response = outbound_answer()
        elif t == 'event':
            event = body['body-json']
            caller_uuid = db.Table("AgentCalls").get_item(Key={ 'uuid': event['uuid']})['Item']['caller_uuid']
            caller_data = db.Table('SamanaNexmo').get_item(Key={ 'uuid': caller_uuid })['Item']
            print "caller_data: " + json.dumps(caller_data)
            if 'dtmf' in event:
                response = outbound_dtmf(event, caller_data, db)
            else:
                response = {
                    'started': outbound_started,
                    'ringing': outbound_ringing,
                    'answered': outbound_answered,
                    'machine': outbound_machine,
                    'completed': outbound_completed,
                    'timeout': outbound_timeout,
                    'failed': outbound_failed,
                    'rejected': outbound_rejected,
                    'unanswered': outbound_unanswered,
                    'busy': outbound_busy
                }[event['status']](event, caller_data, db)
        else:
            raise KeyError("action={}".format(t))
    except Exception as e:
        response = { "error": "Error in parameter {}".format(e.args[0]) }
    finally:
        return response

def outbound_answer():
    try:
        print sys._getframe().f_code.co_name
        response = [
            { 
                "action": "stream",
                "streamUrl": [ os.environ['silence1s'] ]
            },
            {
                "action": "talk",
                "text": os.environ['agent_welcome']
            },
            {
                "action": "talk",
                "text": os.environ['agent_accept'],
                "bargeIn": True
            },
            {
                "action": "input",
                "maxDigits": 1,
                "eventUrl": [ "https://9vpr0y3928.execute-api.us-east-1.amazonaws.com/dev/event/outbound" ]
            }]
    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "OS variable {} not set".format(e.args[0])
        }
    finally:
        return response

def outbound_dtmf(event, caller_data, db):
    try:
        print sys._getframe().f_code.co_name + " " + json.dumps(event) + " " + json.dumps(caller_data)
        if event['timed_out']:
            db.Table("AgentCalls").update_item(
                Key                      = { "uuid": event['uuid'] },
                UpdateExpression         = "set #s = :s",
                ExpressionAttributeValues= { 
                    ":s": 'rejected'
                    },
                ExpressionAttributeNames = { 
                    "#s": "status"
                    },
                ReturnValues="UPDATED_NEW")
            response = {}
        else:
            response = [
                {
                    "action": "talk",
                    "text": os.environ['agent_placeintoconf']
                },
                {
                    "action": "conversation",
                    "name": "samana-support",
                    "startOnEnter": True
                }]
            db.Table("SamanaNexmo").update_item(
                Key                      = { "uuid": caller_data['uuid'] },
                UpdateExpression         = "set #a = :a, #s = :s",
                ExpressionAttributeValues= {
                    ":a": True,
                    ":s": "incall"
                    },
                ExpressionAttributeNames = { 
                    "#a": "answered",
                    "#s": "status"
                    },
                ReturnValues="UPDATED_NEW")

    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0])
        }
    except Exception as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": e.args[0],
            "errortype": str(type(e)),
        }
    finally:
        return response

def outbound_answered(event, caller_data, db):
    try:
        print sys._getframe().f_code.co_name + " " + json.dumps(event) + " " + json.dumps(caller_data)
        db.Table("AgentCalls").update_item(
            Key                      = { "uuid": event['uuid'] },
            UpdateExpression         = "set #s = :s",
            ExpressionAttributeValues= { ":s": event['status'] },
            ExpressionAttributeNames = { "#s": "status" },
            ReturnValues             = "UPDATED_NEW")
        response = {}
    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0])
        }
    except Exception as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": e.args[0],
            "errortype": str(type(e)),
        }
    finally:
        return response

def outbound_started(event, caller_data, db):
    print sys._getframe().f_code.co_name + " " + json.dumps(event) + " " + json.dumps(caller_data)
    return {}

def outbound_ringing(event, caller_data, db):
    try:
        print sys._getframe().f_code.co_name + " " + json.dumps(event) + " " + json.dumps(caller_data)
        table = db.Table("AgentCalls")
        table.update_item(
            Key                      = { "uuid": event['uuid'] },
            UpdateExpression         = "set #s = :s",
            ExpressionAttributeValues= { ":s": event['status'] },
            ExpressionAttributeNames = { "#s": "status" },
            ReturnValues             = "UPDATED_NEW")
        response = {}
    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0])
        }
    except Exception as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": e.args[0],
            "errortype": str(type(e)),
        }
    finally:
        return response

def outbound_machine(event, caller_data, db):
    print sys._getframe().f_code.co_name + " " + json.dumps(event) + " " + json.dumps(caller_data)
    return {}

def outbound_completed(event, caller_data, db):
    try:
        print sys._getframe().f_code.co_name + " " + json.dumps(event) + " " + json.dumps(caller_data)
        table = db.Table("AgentCalls")
        response = {}
        retry = False
        status = "completed"

        if caller_data['status'] == 'waiting' and not caller_data['answered']:
            retry = True
            status = None

        ue = "set #d = :d"
        eav = { ":d": event['duration'] }
        ean = { "#d": "duration" }
        if "start_time" in event and event['start_time'] is not None:
            ue = ue + ", #st = :st"
            eav[':st'] = event['start_time']
            ean['#st'] = "start_time"
        if "end_time" in event and event['end_time'] is not None:
            ue = ue + ", #et = :et"
            eav[':et'] = event['end_time']
            ean['#et'] = "end_time"
        if status is not None:
            ue = ue + ", #s = :s"
            eav[":s"] = status
            ean["#s"]  = "status"

        table.update_item(
            Key                      = { "uuid": event['uuid'] },
            UpdateExpression         = ue,
            ExpressionAttributeValues= eav,
            ExpressionAttributeNames = ean,
            ReturnValues             = "UPDATED_NEW")

        if retry:
            response = call_agent(event, caller_data, db)
    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0])
        }
    except Exception as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": e.args[0],
            "errortype": str(type(e)),
        }
    finally:
        return response

def outbound_timeout(event, caller_data, db):
    try:
        print sys._getframe().f_code.co_name + " " + json.dumps(event) + " " + json.dumps(caller_data)
        table = db.Table("AgentCalls")
        table.update_item(
            Key                      = { "uuid": event['uuid'] },
            UpdateExpression         = "set #s = :s",
            ExpressionAttributeValues= { ":s": event['status'] },
            ExpressionAttributeNames = { "#s": "status" },
            ReturnValues             = "UPDATED_NEW")
        response = {}
    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0])
        }
    except Exception as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": e.args[0],
            "errortype": str(type(e)),
        }
    finally:
        return response

def outbound_failed(event, caller_data, db):
    try:
        print sys._getframe().f_code.co_name + " " + json.dumps(event) + " " + json.dumps(caller_data)
        table = db.Table("AgentCalls")
        table.update_item(
            Key                      = { "uuid": event['uuid'] },
            UpdateExpression         = "set #s = :s",
            ExpressionAttributeValues= { ":s": event['status'] },
            ExpressionAttributeNames = { "#s": "status" },
            ReturnValues="UPDATED_NEW")
        if caller_data['status'] == 'waiting':
            response = call_agent(event, caller_data, db)
        else:
            response = {}
    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0])
        }
    except Exception as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": e.args[0],
            "errortype": str(type(e)),
        }
    finally:
        return response

def outbound_rejected(event, caller_data, db):
    try:
        print sys._getframe().f_code.co_name + " " + json.dumps(event) + " " + json.dumps(caller_data)
        table = db.Table("AgentCalls")
        table.update_item(
            Key                      = { "uuid": event['uuid'] },
            UpdateExpression         = "set #s = :s",
            ExpressionAttributeValues= { ":s": event['status'] },
            ExpressionAttributeNames = { "#s": "status" },
            ReturnValues="UPDATED_NEW")
        if caller_data['status'] == 'waiting':
            response = call_agent(event, caller_data, db)
        else:
            response = {}
    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0])
        }
    except Exception as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": e.args[0],
            "errortype": str(type(e)),
        }
    finally:
        return response

def outbound_unanswered(event, caller_data, db):
    try:
        print sys._getframe().f_code.co_name + " " + json.dumps(event) + " " + json.dumps(caller_data)
        table = db.Table("AgentCalls")
        table.update_item(
            Key                      = { "uuid": event['uuid'] },
            UpdateExpression         = "set #s = :s",
            ExpressionAttributeValues= { ":s": event['status'] },
            ExpressionAttributeNames = { "#s": "status" },
            ReturnValues="UPDATED_NEW")
        if caller_data['status'] == 'waiting':
            response = call_agent(event, caller_data, db)
        else:
            response = {}
    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0])
        }
    except Exception as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": e.args[0],
            "errortype": str(type(e)),
        }
    finally:
        return response

def outbound_busy(event, caller_data, db):
    try:
        print sys._getframe().f_code.co_name + " " + json.dumps(event) + " " + json.dumps(caller_data)
        table = db.Table("AgentCalls")
        table.update_item(
            Key                      = { "uuid": event['uuid'] },
            UpdateExpression         = "set #s = :s",
            ExpressionAttributeValues= { ":s": event['status'] },
            ExpressionAttributeNames = { "#s": "status" },
            ReturnValues="UPDATED_NEW")
        if caller_data['status'] == 'waiting':
            response = call_agent(caller_data, caller_data, db)
        else:
            response = {}
    except KeyError as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": "Error in parameter {}".format(e.args[0])
        }
    except Exception as e:
        response = { 
            "function": sys._getframe().f_code.co_name, 
            "error": e.args[0],
            "errortype": str(type(e)),
        }
    finally:
        return response

def test_get_phones(event, context):
    return re.sub('[^0-9]', '', get_phones()[0])

def get_phones():
    client_id     = os.environ['podio_client_id'];
    client_secret = os.environ['podio_client_secret'];
    s_app_id      = os.environ['podio_s_app_id']; # Staffing app
    s_app_token   = os.environ['podio_s_app_token']; # Staffing token
    view_id       = os.environ['podio_view_id']; # This week on Call view
    field_id      = os.environ['podio_field_id']; # Assignment

    c = api.OAuthAppClient(
        client_id, 
        client_secret, 
        s_app_id, 
        s_app_token,
    )
    item_id = c.Item.filter_by_view(s_app_id, view_id)['items'][0]['item_id']
    user_data = c.Item.values(item_id)

    phones = []
    for u in user_data:
        if 'external_id' in u and u['external_id'] == 'meeting-participants':
            for v in u['values']:
                if 'value' in v and 'phone' in v['value']:
                    phones += v['value']['phone']
    return phones

