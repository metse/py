import json
from requests import get
from pprint import pprint

response = get("[redacted]")
data = response.text 
json_data = json.loads(data)
pprint(json_data)