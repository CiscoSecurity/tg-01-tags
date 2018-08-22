import requests

api_key = 'asdf1234asdf1234asdf1234'

# EXAMPLE:
# domain = 'cisco.com'
domain = '<DOMAIN>'

url = 'https://panacea.threatgrid.com/api/v2/domains/{}/tags?api_key={}'.format(domain, api_key)

r = requests.get(url)

print(r.json())
