from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

imc_global = None
classificacao_global = None

@app.route('/api', methods=['POST', 'GET'])
def postma():
    global imc_global, classificacao_global

    if request.method == 'POST':
        data = request.get_json()
        print(data)
        peso = float(data["peso"])
        altura = float(data["altura"])

        imc = peso / (altura ** 2)

        # Enviar o IMC para a outra API Node.js
        response_node = requests.post('http://localhost:3000/verificar-imc', json={'imc': imc})

        if response_node.status_code == 200:
            data_node = response_node.json()
            
            imc_global = data_node.get('imc')
            classificacao_global = data_node.get('classificacao')

            return jsonify({'message': f'Seu IMC é {str(imc)}!'})
        else:
            return jsonify({'message': f'Erro na requisição para a API Node.js: {response_node.status_code}'})

    elif request.method == 'GET':
        return jsonify({'imc': imc_global, 'classificacao': classificacao_global})
    else:
        return jsonify({'message': f'Método não permitido'})

if __name__ == '__main__':
    app.run(debug=True)
