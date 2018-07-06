import requests

api_key = 'ujvti7c23leqcuaomc24nmdev6'

sample_id = 'cc3d13fe82aa07f67fee5ae8346adfa6'

tag = 'MyTag'

url = 'https://panacea.threatgrid.com/api/v2/samples/{}/tag?api_key={}&tag={}'.format(sample_id,api_key,tag)

r = requests.post(url)

print r.json()
