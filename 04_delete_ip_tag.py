import requests

api_key = 'asdf1234asdf1234asdf1234'

ip_address = '<IP_ADDRESS>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/ips/{}/tag/{}?api_key={}'.format(ip_address, tag, api_key)

r = requests.delete(url)

print(r.status_code)
