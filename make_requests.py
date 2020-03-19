import json
import urllib.request
import urllib.parse
import requests

a = 0
offset_count = 1
token = INSTERT TOKEN HERE
while a <= 39:
	name = ("location_" + str(a))
	url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=' +str(offset_count)
	header = {"token": token,
	            'Content-Type' :  'application/json'}
	#r = requests.get(url, headers= headers)
	request = requests.get(url, headers = header)
	data = request.json()

	with open ((name + ".json"), 'w') as outfile:
		json.dump(data, outfile)
	a = a + 1
	offset_count = offset_count + 1000


