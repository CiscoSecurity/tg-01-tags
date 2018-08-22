import requests

api_key = 'asdf1234asdf1234asdf1234'

# EXAMPLE:
# domain = 'cisco.com'
domain = '<DOMAIN>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/domains/{}/tag?api_key={}&tag={}'.format(domain, api_key, tag)

r = requests.post(url)

print(r.json())
