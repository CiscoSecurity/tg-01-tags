import requests
import hashlib

api_key = 'asdf1234asdf1234asdf1234'

# The 'b' before the string required to properly calculate the SHA256
# https://www.python.org/dev/peps/pep-3112/
# https://docs.python.org/3/reference/lexical_analysis.html#strings
# EXAMPLE:
# url = b'http://cisco.com:80/'
url = b'<URL>'
url_sha256 = hashlib.sha256(url).hexdigest()

url = 'https://panacea.threatgrid.com/api/v2/urls/{}/tags?api_key={}'.format(url_sha256, api_key)

r = requests.get(url)

print(r.json())
