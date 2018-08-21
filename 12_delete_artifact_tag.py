import requests

api_key = 'asdf1234asdf1234asdf1234'

artifact_sha256 = '<ARTIFACT_SHA56>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/artifacts/{}/tag/{}?api_key={}'.format(artifact_sha256, tag, api_key)

r = requests.delete(url)

print(r.status_code)
