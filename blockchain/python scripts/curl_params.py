import requests
import json

payload= {"address":"n1i3ToCvRr85Mfu3CRH7Bz4tuGGgrHaacn2"}
headers = {'Content-Type: application/json'}
r=requests.post("http://localhost:8685/v1/user/accountstate ", data=json.dumps(payload),headers= headers)

print "r.text : ", r.text


