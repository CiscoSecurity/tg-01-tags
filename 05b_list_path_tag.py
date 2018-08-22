import requests

api_key = 'asdf1234asdf1234asdf1234'

# EXAMPLE:
# path = '\TEMP\Tags.reg'
path = '<PATH>'

url = 'https://panacea.threatgrid.com/api/v2/paths/{}/tags?api_key={}'.format(path, api_key)

r = requests.get(url)

print(r.json())
