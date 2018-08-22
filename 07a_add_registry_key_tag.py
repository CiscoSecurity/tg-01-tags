import requests

api_key = 'asdf1234asdf1234asdf1234'

# EXAMPLE:
# registry_key = 'MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Tags'
registry_key = '<REGISTRY_KEY>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/registry_keys/{}/tag?api_key={}&tag={}'.format(registry_key, api_key, tag)

r = requests.post(url)

print(r.json())
