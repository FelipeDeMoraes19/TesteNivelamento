import pdfplumber
import pandas as pd
import os
from zipfile import ZipFile
from concurrent.futures import ThreadPoolExecutor

PDF_PATH = "../downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
CSV_PATH = "../dados_csv/resultado.csv"
ZIP_PATH = "../compactado/Teste_Felipe.zip"

def criar_diretorios():
    os.makedirs(os.path.dirname(CSV_PATH), exist_ok=True)
    os.makedirs(os.path.dirname(ZIP_PATH), exist_ok=True)

def extrair_tabela_pagina(page):
    tabela = page.extract_table()
    return tabela if tabela else []

def extrair_tabelas_do_pdf(pdf_path):
    dados = []
    with pdfplumber.open(pdf_path) as pdf:
        with ThreadPoolExecutor(max_workers=4) as executor:
            resultados = executor.map(extrair_tabela_pagina, pdf.pages)
            for tabela in resultados:
                dados.extend(tabela)
    return dados

def tratar_dados(dados_brutos):
    cabecalho = dados_brutos[0]
    dados = dados_brutos[1:]

    df = pd.DataFrame(dados, columns=cabecalho)

    df.rename(columns={
        'OD': 'Seg. Odontológica',
        'AMB': 'Seg. Ambulatorial'
    }, inplace=True)

    return df

def salvar_csv(df, csv_path):
    df.to_csv(csv_path, index=False)
    print(f" Arquivo CSV salvo em: {csv_path}")

def compactar_csv(csv_path, zip_path):
    """Compacta o CSV gerado em um arquivo ZIP."""
    with ZipFile(zip_path, 'w') as zipf:
        zipf.write(csv_path, arcname=os.path.basename(csv_path))
    print(f" CSV compactado com sucesso em: {zip_path}")

def testes_adicionais(df, csv_path, zip_path):
    print("\n Executando testes adicionais...")
    assert not df.empty, "O DataFrame está vazio."
    assert os.path.exists(csv_path), "CSV não encontrado após salvar."
    assert os.path.exists(zip_path), "ZIP não encontrado após compactação."
    print(" Todos os testes passaram com sucesso!")

def main():
    try:
        criar_diretorios()

        print(" Extraindo dados do PDF com paralelismo...")
        dados_brutos = extrair_tabelas_do_pdf(PDF_PATH)

        print(" Tratando os dados extraídos...")
        df = tratar_dados(dados_brutos)

        print(" Salvando dados em CSV...")
        salvar_csv(df, CSV_PATH)

        print("🗜️ Compactando CSV...")
        compactar_csv(CSV_PATH, ZIP_PATH)

        testes_adicionais(df, CSV_PATH, ZIP_PATH)

    except Exception as e:
        print(f"❌ Erro durante execução: {e}")

if __name__ == "__main__":
    main()
