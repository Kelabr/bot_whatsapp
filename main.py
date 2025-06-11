import requests

url = "http://localhost:8080/message/sendText/kekel"
numbers = ["5513981151688"]

for n in numbers:
    payload = {
    "number":n,
    "textMessage": {"text": "Fala bichinha, sou o bot do Kelvin, ele pediu pata fazer um banco de dados para ele, Por favor"}
    }   
    headers = {
        "apikey": "123",
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    print(response.text)




