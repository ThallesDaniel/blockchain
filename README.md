# Web3 Bitcoin Miner & Blockchain Study Project

## Descrição

Este é um projeto de estudo sobre desenvolvimento Web3, no qual explorei a criação de um minerador de Bitcoin utilizando Python. Além disso, desenvolvi minha própria blockchain na pasta `blockchain/`, utilizando as tecnologias **Truffle**, **Ganache** e **Web3.js**.

O objetivo do projeto é compreender melhor o funcionamento de criptomoedas, contratos inteligentes e o ecossistema descentralizado.

## Tecnologias Utilizadas

- **Python**: Para desenvolvimento do minerador de Bitcoin.
- **Truffle**: Framework para desenvolvimento, teste e implantação de contratos inteligentes.
- **Ganache**: Ambiente de blockchain privado para testes e desenvolvimento.
- **Web3.js**: Biblioteca para interagir com a blockchain via JavaScript.

## Estrutura do Projeto

```
/web3-bitcoin-miner
│── minerador/          # Código do minerador de Bitcoin em Python
│── blockchain/         # Implementação da blockchain com Truffle e Web3.js
│── README.md          # Documentação do projeto
```

## Como Executar

### 1. Executar o Minerador de Bitcoin
Certifique-se de ter o **Python** instalado e execute:
```sh
cd minerador
python minerador.py
```

### 2. Configurar e Executar a Blockchain

1. Instale as dependências:
```sh
npm install -g truffle
npm install web3
```

2. Inicie o Ganache para um ambiente blockchain local.
3. Compile e implante os contratos inteligentes:
```sh
cd blockchain
truffle compile
truffle migrate --network development
```

## Conclusão

Este projeto serviu como uma base para estudos sobre tecnologias Web3 e blockchain. A mineração e a criação de uma blockchain são conceitos fundamentais para compreensão do ecossistema das criptomoedas.

Sinta-se à vontade para explorar e modificar o código!

