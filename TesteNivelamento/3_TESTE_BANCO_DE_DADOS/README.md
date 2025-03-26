# Teste 3: Banco de Dados 

Criação e consulta analítica em banco PostgreSQL.

## Funcionalidades

- Estruturação das tabelas necessárias.
- Importação automática de CSVs.
- Consultas analíticas.

## Como executar com Docker 🐳

```bash
cd 3_TESTE_BANCO_DE_DADOS
```

```bash
docker-compose up -d
```

# Conectar ao banco (psql):

```bash
psql -h localhost -U teste -d ansdb
```

## Execução das queries:
```sql
-- Criar tabelas
\i scripts_sql/01_criar_tabelas.sql

-- Importar dados
\i scripts_sql/02_importar_dados.sql

-- Consultas analíticas
\i scripts_sql/03_consultas_analiticas.sql

```

## Estrutura SQL:

- `01_criar_tabelas.sql:` Cria tabelas.

- `02_importar_dados.sql:` Importa CSV para tabelas.

- `03_consultas_analiticas.sql:` Consultas para top-10 despesas.