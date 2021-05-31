import json
from requests import get
from pprint import pprint

response = get("https://api.chucknorris.io/jokes/random")
data = response.text 
json_data = json.loads(data)
pprint(json_data)