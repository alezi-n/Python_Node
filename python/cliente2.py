import requests

url = "http://127.0.0.1:5000/api"

peso = input("Qual seu peso?\n")
altura = input("Qual sua altura?\n")

data = {"peso": peso, "altura": altura}

response = requests.post(url, json=data)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erro na requisição: {response.status_code}")

url_node = 'http://localhost:3000/verificar-imc'
response_node = requests.get(url_node)

if response_node.status_code == 200:
    data_node = response_node.json()
    print(data_node)
else:
    print(f"Erro na requisição: {response_node.status_code}")
