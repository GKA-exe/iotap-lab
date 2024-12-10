import requests
import json
payload = {'text': 'I Love Earth'}
header = {'Content-type': 'application/json'}
res = requests.post(url="http://localhost:5000/api", data=json.dumps(payload), headers=header)
print(res.text)