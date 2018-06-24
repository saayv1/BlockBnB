import requests
import json

payload= {"transaction" : {"from": "n1FF1nz6tarkDVwWQkMnnwFPuPKUaQTdptE","to":"n1i3ToCvRr85Mfu3CRH7Bz4tuGGgrHaacn2","value":"100","nonce":8,"gasPrice":"1000000","gasLimit":"2000000","contract":{"function":"save","args":"[150]"}},"passphrase":"passphrase"}
headers = {'Content-Type: application/json'}
r=requests.post("http://localhost:8685/v1/admin/transactionWithPassphrase ", data=json.dumps(payload),headers= headers)

print ("r.text : ", r.text)
