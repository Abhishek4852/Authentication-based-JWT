import requests,json

url = "http://127.0.0.1:5000/verify"

data= {'token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InZpY2tleXkiLCJleHAiOjE3MTkxNTM1Mjd9.Jpx38ln5nIMf8STu3d-c7gm65S6cgy0JltvkrrkPZ3I',
}

respons = requests.post(url,json=data)

print(respons.json())
