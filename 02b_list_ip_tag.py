import requests

api_key = 'asdf1234asdf1234asdf1234'

# EXAMPLE:
# ip_address = '193.70.19.218'
ip_address = '<IP_ADDRESS>'

url = 'https://panacea.threatgrid.com/api/v2/ips/{}/tags?api_key={}'.format(ip_address, api_key)

r = requests.get(url)

print(r.json())
