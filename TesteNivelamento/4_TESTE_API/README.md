# Teste 4: API com Vue.js + FastAPI 

Desenvolvimento de uma aplicação web com **interface em Vue.js** conectada a uma **API em FastAPI**, consumindo dados de um arquivo CSV.

---

## Funcionalidades

- Servidor FastAPI com endpoint de busca textual.
- Interface Vue.js com campo de busca interativa.
- Containerização com Docker (frontend + backend).
- Coleção Postman para testar a API.

---

## Como executar com Docker 🐳

```bash
cd 4_TESTE_API
docker-compose up --build -d
```

# Acessos após subir os containers:

`Backend (FastAPI):`
http://localhost:8000/buscar/?texto=unimed

`Frontend:`
http://localhost:3000 ou http://localhost:5173

`Exemplo de Rota de busca:` GET /buscar/?texto=unimed

*Obs: A porta 5173 é usada apenas no modo desenvolvimento com npm run dev. No Docker, o build é feito com vite build + serve, rodando na porta 3000.*

# Estrutura do Projeto

`backend/main.py:` FastAPI + pandas para leitura e filtro do CSV.

`backend/Relatorio_cadop.csv:` Arquivo base com cadastros de operadoras.

`frontend/vue-project:` Interface com campo de busca e listagem.

`docker-compose.yml:` Orquestra frontend e backend.

`TesteNivelamento_API.postman_collection.json:` Coleção Postman pronta para uso.

*Observações*

- O `frontend` utiliza `axios` para consumo da API.

- A busca considera `qualquer campo` que contenha o texto (case-insensitive).

- O `backend` garante retorno compatível com `JSON` mesmo em casos com `NaN` ou `inf`.

