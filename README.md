# 🚗 API de Carros com Flask

Este projeto é uma **API REST simples** desenvolvida em **Python + Flask**, criada para simular a interação com um "banco de dados" de carros, utilizando uma lista em memória (`bd.py`).  
O objetivo é demonstrar os conceitos básicos de **CRUD (Create, Read, Delete)** e a estrutura de uma aplicação Flask modular.

---

## 🎯 Objetivo do Projeto

Criar uma API funcional que:
- Liste todos os carros disponíveis;
- Retorne um carro específico pelo seu ID;
- Permita cadastrar (POST) um novo carro;
- Permita deletar (DELETE) um carro existente.

Tudo isso sem utilizar um banco de dados real, apenas manipulando uma lista de dicionários em Python.

---

## 🧩 Estrutura do Projeto

📂 api-carros
┣ 📜 main.py # Arquivo principal, inicializa o servidor Flask e define as rotas
┣ 📜 bd.py # "Banco de dados" simulado com uma lista de dicionários
┣ 📜 requirements.txt # Dependências do projeto
┗ 📜 README.md # Este arquivo 😄

---

## ⚙️ Tecnologias Utilizadas

- 🐍 **Python 3.x**
- 🌶️ **Flask** — microframework web para criação de APIs
- 💾 **Lista de dicionários** como banco de dados em memória

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório
```bash
git clone https://github.com/seuusuario/api-carros.git
cd api-carros
```

### 2. Criar e ativar um ambiente virtual (opcional, mas recomendado)
```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```
### 3. Instalar dependências
```
pip install flask
```

### Ou se tiver o arquivo requirements.txt:
```
pip install -r requirements.txt
```

### 4. Executar o servidor
```
python main.py
```

O Flask iniciará em:
```
http://localhost:5000
```

## 🔗 Endpoints da API
### 🟢 GET /carros

Retorna a lista de todos os carros.

Exemplo de resposta:
```
[
  {"id": 1, "marca": "Toyota", "modelo": "Corolla", "ano": 2021, "cor": "Prata", "preco": 118000},
  {"id": 2, "marca": "Honda", "modelo": "Civic", "ano": 2020, "cor": "Preto", "preco": 110000}
]
```

### 🟢 GET /carros/<id>

Retorna um carro específico pelo ID.

Exemplo:
```
GET /carros/5
```
Resposta:
```
{
  "mensagem": "Carro específico",
  "carro": {
    "id": 5,
    "marca": "Volkswagen",
    "modelo": "Gol",
    "ano": 2018,
    "cor": "Vermelho",
    "preco": 42000
  }
}

```

### 🟡 POST /carros

Adiciona um novo carro à lista.

Exemplo de corpo da requisição (JSON):
```
{
  "marca": "Fiat",
  "modelo": "Argo",
  "ano": 2023,
  "cor": "Branco",
  "preco": 72000
}

```
Resposta:
```
{
  "mensagem": "Carro adicionado com sucesso",
  "carro": { ...novo carro... }
}
```

### 🔴 DELETE /carros/<id>

Remove um carro existente da lista.

Exemplo:
```
DELETE /carros/3
```
Resposta:
```
{
  "mensagem": "Carro removido com sucesso",
  "carro": { ...carro removido... }
}
```

## 🧠 Conceitos Envolvidos

Estrutura básica de uma API REST

Manipulação de listas e dicionários em Python

Uso de rotas dinâmicas no Flask (/carros/<int:id>)

Retorno de respostas JSON

Boas práticas de status HTTP (200, 404, etc.)

## 💡 Possíveis Melhorias Futuras

Implementar PUT /carros/<id> (para atualizar um carro)

Persistir dados em um banco de dados real (SQLite, PostgreSQL ou Oracle)

Adicionar validação de entrada (com Flask-RESTful ou Marshmallow)

Criar testes automatizados com pytest
