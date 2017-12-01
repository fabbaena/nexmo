import sys
import lambda_function

event_answer = {
  "params": {
    "path": {},
    "querystring": {},
    "header": {}
  },
  "stage-variables": {},
  "context": {
    "cognito-authentication-type": "",
    "http-method": "GET",
    "account-id": "438136544486",
    "resource-path": "/answer/inbound",
    "authorizer-principal-id": "",
    "user-arn": "arn:aws:iam::438136544486:root",
    "request-id": "test-invoke-request",
    "source-ip": "test-invoke-source-ip",
    "caller": "438136544486",
    "api-key": "test-invoke-api-key",
    "user-agent": "Apache-HttpClient/4.5.x (Java/1.8.0_144)",
    "user": "438136544486",
    "cognito-identity-pool-id": "",
    "api-id": "9vpr0y3928",
    "resource-id": "wwmzkb",
    "stage": "test-invoke-stage",
    "cognito-identity-id": "",
    "cognito-authentication-provider": ""
  }
}

event_ringing = {
  "body-json": {
    "uuid": "uuid1",
    "conversation_uuid": "convers_uuid",
    "status": "ringing",
    "direction": "inbound"
  },
  "params": {
    "path": {},
    "querystring": {},
    "header": {}
  },
  "stage-variables": {},
  "context": {
    "cognito-authentication-type": "",
    "http-method": "POST",
    "account-id": "438136544486",
    "resource-path": "/event/inbound",
    "authorizer-principal-id": "",
    "user-arn": "arn:aws:iam::438136544486:root",
    "request-id": "test-invoke-request",
    "source-ip": "test-invoke-source-ip",
    "caller": "438136544486",
    "api-key": "test-invoke-api-key",
    "user-agent": "Apache-HttpClient/4.5.x (Java/1.8.0_144)",
    "user": "438136544486",
    "cognito-identity-pool-id": "",
    "api-id": "9vpr0y3928",
    "resource-id": "wwmzkb",
    "stage": "test-invoke-stage",
    "cognito-identity-id": "",
    "cognito-authentication-provider": ""
  }
}

event_answered = {
  "body-json": {
    "start_time": "",
    "rate": "",
    "from": "12341234",
    "to": "09870987",
    "uuid": "uuid1",
    "conversation_uuid": "convers_uuid",
    "status": "answered",
    "direction": "inbound",
    "network": ""
  },
  "params": {
    "path": {},
    "querystring": {},
    "header": {}
  },
  "stage-variables": {},
  "context": {
    "cognito-authentication-type": "",
    "http-method": "POST",
    "account-id": "438136544486",
    "resource-path": "/event/inbound",
    "authorizer-principal-id": "",
    "user-arn": "arn:aws:iam::438136544486:root",
    "request-id": "test-invoke-request",
    "source-ip": "test-invoke-source-ip",
    "caller": "438136544486",
    "api-key": "test-invoke-api-key",
    "user-agent": "Apache-HttpClient/4.5.x (Java/1.8.0_144)",
    "user": "438136544486",
    "cognito-identity-pool-id": "",
    "api-id": "9vpr0y3928",
    "resource-id": "wwmzkb",
    "stage": "test-invoke-stage",
    "cognito-identity-id": "",
    "cognito-authentication-provider": ""
  }
}

event_completed = {
  "body-json": {
    "duration":"116",
    "start_time":"2017-11-29T17:09:24.000Z",
    "rate":"0.00450000",
    "price":"0.00870000",
    "end_time":"2017-11-29T17:11:20.000Z",
    "from":"17863856106","to":"17865903880",
    "uuid":"uuid1",
    "conversation_uuid":"convers_uuid",
    "status":"completed",
    "direction":"inbound",
    "network":"US-FIXED"
  },
  "params": {
    "path": {},
    "querystring": {},
    "header": {}
  },
  "stage-variables": {},
  "context": {
    "cognito-authentication-type": "",
    "http-method": "POST",
    "account-id": "438136544486",
    "resource-path": "/event/inbound",
    "authorizer-principal-id": "",
    "user-arn": "arn:aws:iam::438136544486:root",
    "request-id": "test-invoke-request",
    "source-ip": "test-invoke-source-ip",
    "caller": "438136544486",
    "api-key": "test-invoke-api-key",
    "user-agent": "Apache-HttpClient/4.5.x (Java/1.8.0_144)",
    "user": "438136544486",
    "cognito-identity-pool-id": "",
    "api-id": "9vpr0y3928",
    "resource-id": "wwmzkb",
    "stage": "test-invoke-stage",
    "cognito-identity-id": "",
    "cognito-authentication-provider": ""
  }
}

agent_uuid = "d9509cf3-59e9-4e73-9551-d229f209adeb"
agent_started = {
  "body-json": {
    "uuid":agent_uuid,
    "conversation_uuid":"CON-0f6b7196-5226-45d4-89df-45a9b0a69201",
    "status":"started",
    "direction":"outbound"
  },
  "params": {
    "path": {},
    "querystring": {},
    "header": {}
  },
  "stage-variables": {},
  "context": {
    "cognito-authentication-type": "",
    "http-method": "POST",
    "account-id": "438136544486",
    "resource-path": "/event/outbound",
    "authorizer-principal-id": "",
    "user-arn": "arn:aws:iam::438136544486:root",
    "request-id": "test-invoke-request",
    "source-ip": "test-invoke-source-ip",
    "caller": "438136544486",
    "api-key": "test-invoke-api-key",
    "user-agent": "Apache-HttpClient/4.5.x (Java/1.8.0_144)",
    "user": "438136544486",
    "cognito-identity-pool-id": "",
    "api-id": "9vpr0y3928",
    "resource-id": "wwmzkb",
    "stage": "test-invoke-stage",
    "cognito-identity-id": "",
    "cognito-authentication-provider": ""
  }
}

agent_ringing = {
  "body-json": {
    "uuid":agent_uuid,
    "conversation_uuid":"CON-0f6b7196-5226-45d4-89df-45a9b0a69201",
    "status":"ringing",
    "direction":"outbound"
  },
  "params": {
    "path": {},
    "querystring": {},
    "header": {}
  },
  "stage-variables": {},
  "context": {
    "cognito-authentication-type": "",
    "http-method": "POST",
    "account-id": "438136544486",
    "resource-path": "/event/outbound",
    "authorizer-principal-id": "",
    "user-arn": "arn:aws:iam::438136544486:root",
    "request-id": "test-invoke-request",
    "source-ip": "test-invoke-source-ip",
    "caller": "438136544486",
    "api-key": "test-invoke-api-key",
    "user-agent": "Apache-HttpClient/4.5.x (Java/1.8.0_144)",
    "user": "438136544486",
    "cognito-identity-pool-id": "",
    "api-id": "9vpr0y3928",
    "resource-id": "wwmzkb",
    "stage": "test-invoke-stage",
    "cognito-identity-id": "",
    "cognito-authentication-provider": ""
  }
}

agent_answered = {
  "body-json": {
    "start_time": "",
    "rate":0,
    "from":"17865903880",
    "to":"17863856106",
    "uuid":agent_uuid,
    "conversation_uuid":"CON-4c299ae0-afc9-46d2-ad35-74ea258f73d2",
    "status":"answered",
    "direction":"outbound",
    "network": ""
  },
  "params": {
    "path": {},
    "querystring": {},
    "header": {}
  },
  "stage-variables": {},
  "context": {
    "cognito-authentication-type": "",
    "http-method": "POST",
    "account-id": "438136544486",
    "resource-path": "/event/outbound",
    "authorizer-principal-id": "",
    "user-arn": "arn:aws:iam::438136544486:root",
    "request-id": "test-invoke-request",
    "source-ip": "test-invoke-source-ip",
    "caller": "438136544486",
    "api-key": "test-invoke-api-key",
    "user-agent": "Apache-HttpClient/4.5.x (Java/1.8.0_144)",
    "user": "438136544486",
    "cognito-identity-pool-id": "",
    "api-id": "9vpr0y3928",
    "resource-id": "wwmzkb",
    "stage": "test-invoke-stage",
    "cognito-identity-id": "",
    "cognito-authentication-provider": ""
  }
}

agent_answer = {
  "params": {
    "path": {},
    "querystring": {},
    "header": {}
  },
  "stage-variables": {},
  "context": {
    "cognito-authentication-type": "",
    "http-method": "GET",
    "account-id": "438136544486",
    "resource-path": "/answer/outbound",
    "authorizer-principal-id": "",
    "user-arn": "arn:aws:iam::438136544486:root",
    "request-id": "test-invoke-request",
    "source-ip": "test-invoke-source-ip",
    "caller": "438136544486",
    "api-key": "test-invoke-api-key",
    "user-agent": "Apache-HttpClient/4.5.x (Java/1.8.0_144)",
    "user": "438136544486",
    "cognito-identity-pool-id": "",
    "api-id": "9vpr0y3928",
    "resource-id": "wwmzkb",
    "stage": "test-invoke-stage",
    "cognito-identity-id": "",
    "cognito-authentication-provider": ""
  }
}

agent_completed = {
  "body-json": {
    "duration":"1",
    "start_time":"2017-11-29T21:23:33.000Z",
    "rate":"0.01270000",
    "price":"0.00021167",
    "end_time":"2017-11-29T21:23:34.000Z",
    "from":"17865903880",
    "to":"17863856106",
    "uuid":agent_uuid,
    "conversation_uuid":"CON-4c299ae0-afc9-46d2-ad35-74ea258f73d2",
    "status":"completed",
    "direction":"outbound",
    "network":"310004"
  },
  "params": {
    "path": {},
    "querystring": {},
    "header": {}
  },
  "stage-variables": {},
  "context": {
    "cognito-authentication-type": "",
    "http-method": "POST",
    "account-id": "438136544486",
    "resource-path": "/event/outbound",
    "authorizer-principal-id": "",
    "user-arn": "arn:aws:iam::438136544486:root",
    "request-id": "test-invoke-request",
    "source-ip": "test-invoke-source-ip",
    "caller": "438136544486",
    "api-key": "test-invoke-api-key",
    "user-agent": "Apache-HttpClient/4.5.x (Java/1.8.0_144)",
    "user": "438136544486",
    "cognito-identity-pool-id": "",
    "api-id": "9vpr0y3928",
    "resource-id": "wwmzkb",
    "stage": "test-invoke-stage",
    "cognito-identity-id": "",
    "cognito-authentication-provider": ""
  }
}

agent_dtmf = {
    "body-json": {
        "conversation_uuid": "CON-9cc63f28-d999-456d-8010-ed5873eb89c6",
        "uuid": "73a7df12-488f-4130-91ad-2a603d8d4c05",
        "dtmf": "1",
        "timed_out": False
    },
    "params": {
        "path": {},
        "querystring": {},
        "header": {
            "Content-Type": "application/json",
            "Via": "1.1 35d0cb9682c1de5fc36b9654b593db96.cloudfront.net (CloudFront)",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Forwarded-Proto": "https",
            "X-Forwarded-For": "174.36.197.202, 52.46.14.15",
            "CloudFront-Viewer-Country": "US",
            "User-Agent": "Apache-HttpAsyncClient/4.1 (Java/1.8.0_66)",
            "X-Amzn-Trace-Id": "Root=1-5a2045fb-30baca3178f1d3620a211197",
            "Host": "9vpr0y3928.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "Md1fP762dlXJ8HvLXYKFSHg9HqFaXRh5R92iRB0MI5dQbExm2bJUrQ==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "X-Forwarded-Port": "443",
            "CloudFront-Is-Mobile-Viewer": "false"
        }
    },
    "stage-variables": {},
    "context": {
        "cognito-authentication-type": "",
        "http-method": "POST",
        "account-id": "",
        "resource-path": "/event/outbound",
        "authorizer-principal-id": "",
        "user-arn": "",
        "request-id": "99ee504e-d5f7-11e7-955f-e1016447728d",
        "source-ip": "174.36.197.202",
        "caller": "",
        "api-key": "",
        "user-agent": "Apache-HttpAsyncClient/4.1 (Java/1.8.0_66)",
        "user": "",
        "cognito-identity-pool-id": "",
        "api-id": "9vpr0y3928",
        "resource-id": "bddoc6",
        "stage": "dev",
        "cognito-identity-id": "",
        "cognito-authentication-provider": ""
    }
}

if sys.argv[1] == 'answer':
    print lambda_function.handler(event_answer, {})
elif sys.argv[1] == 'ringing':
    print lambda_function.handler(event_ringing, {})
elif sys.argv[1] == 'answered':
    print lambda_function.handler(event_answered, {})
elif sys.argv[1] == 'completed':
    print lambda_function.handler(event_completed, {})
elif sys.argv[1] == 'agent_answer':
    print lambda_function.handler(agent_answer, {})
elif sys.argv[1] == 'agent_ringing':
    print lambda_function.handler(agent_ringing, {})
elif sys.argv[1] == 'agent_answered':
    print lambda_function.handler(agent_answered, {})
elif sys.argv[1] == 'agent_completed':
    print lambda_function.handler(agent_completed, {})
elif sys.argv[1] == 'agent_dtmf':
    print lambda_function.handler(agent_dtmf, {})

