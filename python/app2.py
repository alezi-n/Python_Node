from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/api', methods=['POST','GET'])
def postma():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        peso = float(data["peso"])
        altura = float(data["altura"])

        imc = peso / (altura ** 2)

        # Enviar o IMC para a outra API
        response = requests.post('http://localhost:3000/verificar-imc', json={'imc': imc})

        return jsonify({'message': f'Seu IMC é {str(imc)}!'})
    else:
        return jsonify({'message': f'Esperando o post!'})

if __name__ == '__main__':
    app.run(debug=True)
