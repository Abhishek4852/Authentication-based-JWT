import requests,json

url = "http://127.0.0.1:5000/register"

data= {
    'username':"saket",
    'password':"saket4852@"
}

respons = requests.post(url,json=data)

print(respons.json())
