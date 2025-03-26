import os
import requests
from zipfile import ZipFile
from concurrent.futures import ThreadPoolExecutor, as_completed

LINKS_ANEXOS = [
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf",
    "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos/Anexo_II_DUT_2021_RN_465.2021_RN628.2025_RN629.2025.pdf"
]

DOWNLOAD_PATH = "/downloads"
ZIP_PATH = "/compactado/anexos.zip"

def criar_diretorios():
    os.makedirs(DOWNLOAD_PATH, exist_ok=True)
    os.makedirs(os.path.dirname(ZIP_PATH), exist_ok=True)

def baixar_arquivo(url, caminho_destino):
    response = requests.get(url, timeout=15, stream=True)
    response.raise_for_status()
    with open(caminho_destino, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

def baixar_pdfs(links):
    arquivos_baixados = []

    def download_e_salvar(link):
        nome_arquivo = os.path.join(DOWNLOAD_PATH, link.split('/')[-1])
        baixar_arquivo(link, nome_arquivo)
        return nome_arquivo

    with ThreadPoolExecutor(max_workers=2) as executor:
        future_to_link = {executor.submit(download_e_salvar, link): link for link in links}
        for future in as_completed(future_to_link):
            link = future_to_link[future]
            try:
                arquivo = future.result()
                print(f" Download concluído: {link}")
                arquivos_baixados.append(arquivo)
            except Exception as e:
                print(f"❌ Falha ao baixar {link}: {e}")

    return arquivos_baixados

def compactar_arquivos(arquivos, destino_zip):
    with ZipFile(destino_zip, 'w') as zipf:
        for arquivo in arquivos:
            zipf.write(arquivo, arcname=os.path.basename(arquivo))
    print(f"\n Arquivos compactados com sucesso em: {destino_zip}")

def testes_adicionais(arquivos, zip_path):
    print("\n Executando testes adicionais...")
    assert len(arquivos) == 2, "Número de arquivos baixados incorreto."
    assert all(os.path.exists(arq) for arq in arquivos), "Arquivos baixados não encontrados."
    assert os.path.exists(zip_path), "Arquivo compactado não encontrado."
    print(" Todos os testes passaram com sucesso!")

def main():
    criar_diretorios()

    print(" Iniciando download dos PDFs...")
    arquivos = baixar_pdfs(LINKS_ANEXOS)

    print("\n Compactando PDFs baixados...")
    compactar_arquivos(arquivos, ZIP_PATH)

    testes_adicionais(arquivos, ZIP_PATH)

if __name__ == "__main__":
    main()
