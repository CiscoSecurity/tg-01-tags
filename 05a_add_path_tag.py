import requests

api_key = 'asdf1234asdf1234asdf1234'

# EXAMPLE:
# path = '\TEMP\Tags.reg'
path = '<PATH>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/paths/{}/tag?api_key={}&tag={}'.format(path, api_key, tag)

r = requests.post(url)

print(r.json())
