import requests

api_key = 'asdf1234asdf1234asdf1234'

domain = '<DOMAIN>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/domains/{}/tag/{}?api_key={}'.format(domain, tag, api_key)

r = requests.delete(url)

print(r.status_code)
