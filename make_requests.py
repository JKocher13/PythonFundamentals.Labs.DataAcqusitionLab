import json
import urllib.request
import urllib.parse
import requests

a = 0
offset_count = 1
token = "ZmqmkkvwvZxdtlLSHXkopRdvSoAJtPWa"
while a <= 1:
	name = ("location_" + str(a))
	url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations?location&limit=1000&offset=' + str(offset_count)
	header = {"token": token,
	            'Content-Type' :  'application/json'}
	request = requests.get(url, headers = header)
	print (request)
	data = request.json()
	with open ((name + ".json"), 'w') as outfile:
		json.dump(data, outfile)
	a = a + 1
	offset_count = offset_count + 1000


