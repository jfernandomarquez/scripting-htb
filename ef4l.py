import requests 

import hashlib

s = requests.Session()

response = s.get('http://x.x.x.x:x', stream=True)

print(response.headers)

result = hashlib.md5(str(response.content[169:187],'utf-8').encode())

a = str(response.content[<int limite inf>:<int limite superior>],'utf-8')

m = hashlib.md5()

m.update(a.encode('utf-8'))

postmd5=s.post("http://x.x.x.x:x", data={'hash': m.hexdigest()})

print(postmd5.content)