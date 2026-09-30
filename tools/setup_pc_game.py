import os
import urllib.request
import zipfile

DOWNLOAD_URL = "https://github.com/Unchiga/Yu-Gi-Oh-Forbidden-Memories-Recompiled/releases/download/v0.1.2/yfm-redecomp-v0.1.2-windows.zip"
TARGET_DIR = "pc_game"
ZIP_PATH = os.path.join(TARGET_DIR, "yfm-windows.zip")

def download_and_extract():
    os.makedirs(TARGET_DIR, exist_ok=True)
    print(f"Baixando executável nativo PC de: {DOWNLOAD_URL}...")
    req = urllib.request.Request(DOWNLOAD_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req) as resp, open(ZIP_PATH, "wb") as out_f:
        total = int(resp.headers.get("Content-Length", 0))
        downloaded = 0
        while True:
            chunk = resp.read(65536)
            if not chunk:
                break
            out_f.write(chunk)
            downloaded += len(chunk)
            if total > 0:
                percent = (downloaded / total) * 100
                print(f"\rProgresso: {percent:.1f}% ({downloaded / (1024*1024):.2f} MB)", end="", flush=True)

    print("\nDownload concluído! Extraindo arquivos...")
    with zipfile.ZipFile(ZIP_PATH, "r") as z:
        z.extractall(TARGET_DIR)
        print("Arquivos extraídos:")
        for name in z.namelist():
            print(f"  - {name}")

    if os.path.exists(ZIP_PATH):
        os.remove(ZIP_PATH)
    print("\nConfiguração inicial concluída com sucesso em:", TARGET_DIR)

if __name__ == "__main__":
    download_and_extract()
