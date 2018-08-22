import requests

api_key = 'asdf1234asdf1234asdf1234'

# EXAMPLE:
# registry_key = 'MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Tags'
registry_key = '<REGISTRY_KEY>'

url = 'https://panacea.threatgrid.com/api/v2/registry_keys/{}/tags?api_key={}'.format(registry_key, api_key)

r = requests.get(url)

print(r.json())
