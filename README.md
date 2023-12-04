# Calculadora de IMC com Comunicação entre Flask e Node.js

Este repositório contém uma aplicação simples para calcular o Índice de Massa Corporal (IMC) utilizando duas partes principais: um servidor Flask em Python e um servidor Express.js em Node.js. A comunicação entre eles é realizada por meio de requisições HTTP.

## Configuração e Uso

### 1. Servidor Flask (Python)

Certifique-se de ter o Flask instalado. Caso não tenha, instale utilizando o seguinte comando:

```bash
pip install flask
```

### 2. Servidor Node.js

Certifique-se de ter o Node.js instalado:

```bash
npm install
```

## Estrutura do Projeto
- **'index.js'**: Código do servidor Node.js.

- **'app1.py'**: Código do servidor Flask.

- **'cliente1.py'**: Script Python para interagir com a aplicação.

## Comentários Adicionais
- A comunicação entre o servidor Flask e o servidor Node.js é realizada ao calcular o IMC no servidor Flask, que, por sua vez, envia o resultado para o servidor Node.js.

- O servidor Node.js classifica o IMC e retorna a classificação ao cliente Python.