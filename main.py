import requests

resp = requests.get('http://lzq2022.ddns.net:10000')
with open('test.txt','w' ) as fp:
    fp.write(resp.text)