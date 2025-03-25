# Teste de Web Scraping

Este projeto realiza o download automático dos **Anexos I e II** em formato PDF diretamente do site da Agência Nacional de Saúde Suplementar (ANS) e compacta os arquivos baixados em um único arquivo ZIP.

## 📌 Funcionalidades

- Download automático dos PDFs.
- Compactação automática dos arquivos baixados.
- Testes adicionais para garantir que os downloads e compactação ocorreram corretamente.
- Paralelização para melhorar a performance dos downloads.

## 🚀 Como Executar Localmente

### Pré-requisitos

- Python 3.x instalado.

### Crie um ambiente virtual e ative-o

```
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

### Instale as dependências

```
cd 1_TESTE_WEB_SCRAPING
```

```
cd src
```
* Depois execute:

```
pip install -r requirements.txt
```

### Depois de baixar as depêndencias, execute:

```
python scraping.py
```
# 🐳 Executar usando Docker

### Pré-requisitos:

- Docker instalado na máquina.

## 🚀 Passo a passo:

- Construir e executar com Docker Compose:
```
cd 1_TESTE_WEB_SCRAPING
docker-compose build
docker-compose up
```
* Os arquivos baixados estarão na pasta downloads e o arquivo compactado estará em compactado/anexos.zip.

### Comandos úteis:

- Para remover o container:
```
docker-compose down
```

- Para visualizar logs:
```
docker logs scraping_ans_container
```


# 📦 Bibliotecas Usadas

- requests

- concurrent.futures (biblioteca padrão Python)

- zipfile (biblioteca padrão Python)
