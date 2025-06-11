from fastapi import FastAPI, Request
import requests

app = FastAPI()

EVOLUTION_API = "http://localhost:8080/message/sendText/kekel"
API_KEY = "123"

def enviar_menssage(numero, texto):
    payload = {
        "number":numero,
        "textMessage": {
            "text":texto
        }
    }
    headers = {
        "Content-Type": "application/json",
        "apikey": API_KEY
    }
    response = requests.post(EVOLUTION_API, json=payload, headers=headers)
    print(response.status_code, response.text)

@app.post('/webhook')
async def webhook(request:Request):
    data = await request.json()
    print("Menssagem Recebida:", data)

    try:
        numero = data['data']['key']['remoteJid']
        menssage = data['data']['message']['extendedTextMessage']['text'].strip()

        if menssage == "1":
            enviar_menssage(numero, "Favor descrever sua situação com detalhes, por fvaor. Já irei responder!")
        elif menssage == "2":
            enviar_menssage(numero, "Me conte o que você quer me falar")
        elif menssage == "3":
            enviar_menssage(numero, "Conta tudooo!!")
        else:
            enviar_menssage(numero, "Escolha uma opção 1 - Situação de pagamento  2 - Assuntos Particulares 3 - F-c-a")

    except Exception as e:
        print("Erro ao processar", e)

    return{'status': 'ok'}
       