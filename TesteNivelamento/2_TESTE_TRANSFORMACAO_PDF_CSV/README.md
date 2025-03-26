# Teste 2: Transformação PDF para CSV 

Extrai tabelas de um arquivo PDF da ANS, salva como CSV e compacta em ZIP.

## Funcionalidades

- Extração paralela das tabelas do PDF.
- Tratamento e renomeação de colunas.
- Compactação automática do CSV.

## Como executar com Docker 🐳

*Vá ate a pasta do teste*:

```bash
cd 2_TESTE_TRANSFORMACAO_PDF_CSV
```

```bash
docker-compose build
docker-compose up
```

## Os arquivos estarão disponíveis em:
```bash
dados_csv/resultado.csv

compactado/Teste_Felipe.zip
```

## Dependências

```bash
- Python 3.12

- pdfplumber

- pandas
