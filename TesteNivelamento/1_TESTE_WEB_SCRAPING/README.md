# Teste 1: Web Scraping 

Realiza o download automático dos **Anexos I e II** (PDF) diretamente do site da ANS e compacta em ZIP.

## Funcionalidades

- Download paralelo.
- Compactação automática dos PDFs.

## Como executar com Docker 🐳

*Vá ate a pasta do teste*:

```bash
cd 1_TESTE_WEB_SCRAPING
```

```bash
docker-compose build
docker-compose up
```

## Os arquivos estarão disponíveis em:

```bash
downloads/ (PDFs baixados)

compactado/anexos.zip
```

## Dependências
```bash
- Python 3.12

- requests

