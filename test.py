"""
The test file for getting the data

clinet id = xO4R2rHsERdPPP1jijxPuNV8IYBWQkTE


curl --request POST \
  --url https://dev-pj7dlc7dchlhef5x.us.auth0.com/oauth/token \
  --header 'content-type: application/json' \
  --data '{
    "client_id":"THmOprbaicrGeK3VO9hVnFx0jHiGyOWU",
    "client_secret":"LsKIL3gbkFCpbQcv6KMqpwH_tgGiAevJdOp6JZmobOCVbWu4SxHXZNl5EDfzjP33",
    "audience":"https://dev-pj7dlc7dchlhef5x.us.auth0.com/api/v2/",
    "grant_type":"client_credentials"
  }'




"""

import http.client

conn = http.client.HTTPSConnection("dev-pj7dlc7dchlhef5x.us.auth0.com")

payload = "{\"client_id\":\"THmOprbaicrGeK3VO9hVnFx0jHiGyOWU\",\"client_secret\":\"LsKIL3gbkFCpbQcv6KMqpwH_tgGiAevJdOp6JZmobOCVbWu4SxHXZNl5EDfzjP33\",\"audience\":\"https://dev-pj7dlc7dchlhef5x.us.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))