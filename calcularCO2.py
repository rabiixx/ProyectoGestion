import json
from urllib.request import urlopen


api_url = 'https://api.triptocarbon.xyz/v1/footprint?activity=10&activityType=miles&country=usa&mode=taxi'
response = urlopen(api_url)
data = json.loads(response.read())
print(data['carbonFootprint'])