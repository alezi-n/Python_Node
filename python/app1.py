from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/calcularIMC', methods=['POST'])
def Calcular_imc():
    global imc_global, classificacao_global

    if request.method == 'POST':
        data = request.get_json()
        print(data)
        peso = float(data["peso"])
        altura = float(data["altura"])

        imc = round(peso / (altura ** 2),2)

        # Enviar o IMC para a outra API Node.js
        response_node = requests.get('http://localhost:3000/verificar-imc', json={'imc': imc})

        if response_node.status_code == 200:
            data_node = response_node.json()

            return data_node
        else:
            return jsonify({'message': f'Erro na requisição para a API Node.js: {response_node.status_code}'})

if __name__ == '__main__':
    app.run(debug=True)
