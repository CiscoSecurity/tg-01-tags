import requests

api_key = 'asdf1234asdf1234asdf1234'

# EXAMPLE:
# sample_id = 'cc3d13fe82aa07f67fee5ae8346adfa6'
sample_id = '<SAMPLE_ID>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/samples/{}/tag/{}?api_key={}'.format(sample_id, tag, api_key)

r = requests.delete(url)

print(r.status_code)
