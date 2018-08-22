import requests

api_key = 'asdf1234asdf1234asdf1234'

# EXAMPLE:
# ip_address = '193.70.19.218'
ip_address = '<IP_ADDRESS>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/ips/{}/tag?api_key={}&tag={}'.format(ip_address, api_key, tag)

r = requests.post(url)

print(r.json())
