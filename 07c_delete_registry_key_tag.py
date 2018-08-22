import requests

api_key = 'asdf1234asdf1234asdf1234'

# EXAMPLE:
# registry_key = 'MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Tags'
registry_key = '<REGISTRY_KEY>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/registry_keys/{}/tag/{}?api_key={}'.format(registry_key, tag, api_key)

r = requests.delete(url)

print(r.status_code)
