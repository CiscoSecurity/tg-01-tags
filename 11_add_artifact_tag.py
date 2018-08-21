import requests

api_key = 'asdf1234asdf1234asdf1234'

artifact_sha256 = '<ARTIFACT_SHA56>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/artifacts/{}/tag?api_key={}&tag={}'.format(artifact_sha256, api_key, tag)

r = requests.post(url)

print(r.json())
