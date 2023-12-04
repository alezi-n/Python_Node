const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

let imcGlobal;
let classificacaoGlobal;

app.post('/verificar-imc', (req, res) => {
  const imc = parseFloat(req.body.imc);
  
  // Verificar a classificação do IMC
  let classificacao;
  if (imc < 18.5) {
    classificacao = 'Abaixo do peso';
  } else if (imc >= 18.5 && imc < 24.9) {
    classificacao = 'Peso normal';
  } else if (imc >= 25 && imc < 29.9) {
    classificacao = 'Sobrepeso';
  } else if (imc >= 30 && imc < 34.9) {
    classificacao = 'Obesidade Grau I';
  } else if (imc >= 35 && imc < 39.9) {
    classificacao = 'Obesidade Grau II';
  } else {
    classificacao = 'Obesidade Grau III';
  }

  // Armazenar o IMC e a classificação em variáveis globais
  imcGlobal = imc;
  classificacaoGlobal = classificacao;

  // Enviar a resposta com a classificação
  res.json({ imc: imc, classificacao: classificacao });
});

app.get('/verificar-imc', (req, res) => {
  // Enviar a resposta com o IMC e a classificação
  res.json({ imc: imcGlobal, classificacao: classificacaoGlobal });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});