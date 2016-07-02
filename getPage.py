#Get a page using request

import requests

targetPage = "https://automatetheboringstuff.com/files/rj.txt"

res = requests.get(targetPage)
res.raise_for_status()

print("type =", type(res))
print("Request status = ", res.status_code == requests.codes.ok)
print("Length", len(res.text))
print(res.text[:250])

testFile = open('testFile.txt', 'wb')
for chunk in res.iter_content(100000):
        testFile.write(chunk)

testFile.close()