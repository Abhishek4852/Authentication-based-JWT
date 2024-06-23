import requests,json

url = "http://127.0.0.1:5000/login"

data= {
    'username':"saket",
    'password':"saket4852@"
}

respons = requests.post(url,json=data)

print(respons.json())

# token generated {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNha2V0IiwiZXhwIjoxNzE5MTU0MTczfQ.NN6VLtrRWF9avU-WMkrht9CKU-_uoMgChtZhdyw9yjI'}
