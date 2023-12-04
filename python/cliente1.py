import requests

url_flask = "http://127.0.0.1:5000/api"

peso = input("Qual seu peso?\n")
altura = input("Qual sua altura?\n")

data = {"peso": peso, "altura": altura}

response_flask = requests.post(url_flask, json=data)

if response_flask.status_code == 200:
    data_flask = response_flask.json()
    print(data_flask)

    response_get = requests.get(url_flask)

    if response_get.status_code == 200:
        data_get = response_get.json()
        print(data_get)
    else:
        print(f"Erro na requisição GET para a API Flask: {response_get.status_code}")
else:
    print(f"Erro na requisição POST para a API Flask: {response_flask.status_code}")
