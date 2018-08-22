import requests

api_key = 'asdf1234asdf1234asdf1234'

# EXAMPLE:
# sample_id = 'cc3d13fe82aa07f67fee5ae8346adfa6'
sample_id = '<SAMPLE_ID>'

url = 'https://panacea.threatgrid.com/api/v2/samples/{}/tags?api_key={}'.format(sample_id, api_key)

r = requests.get(url)

print(r.json())
