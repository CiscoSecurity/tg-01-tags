import requests

api_key = 'asdf1234asdf1234asdf1234'

# EXAMPLE:
# artifact_sha256 = 'c731e5c3f9425d415b15fb961e38aaa7f59125b4fe1c977b594e6e2638b23c2d'
artifact_sha256 = '<ARTIFACT_SHA56>'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/artifacts/{}/tag?api_key={}&tag={}'.format(artifact_sha256, api_key, tag)

r = requests.post(url)

print(r.json())
