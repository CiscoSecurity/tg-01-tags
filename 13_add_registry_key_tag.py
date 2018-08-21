import requests

api_key = 'asdf1234asdf1234asdf1234'

registry_key = '<REGISTRY_KEY>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/registry_keys/{}/tag?api_key={}&tag={}'.format(registry_key, api_key, tag)

r = requests.post(url)

print(r.json())
