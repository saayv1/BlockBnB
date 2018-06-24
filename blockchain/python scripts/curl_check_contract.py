import requests
import json

payload= {"hash":"cfd10b19b290089ef236e8d19cdccd321f87855c76389cd1bc2835b4a433574f"}
headers = {'Content-Type: application/json'}
r=requests.post("http://localhost:8685/v1/user/getTransactionReceipt ", data=json.dumps(payload),headers= headers)

print ("r.text : ", r.text)
