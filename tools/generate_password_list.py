import os
import re
import struct

ROM_PATH = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (PT-BR).bin")
HTML_PATH = r"C:\Users\Gustavo\.gemini\antigravity-ide\brain\6a692b7b-e5b3-4402-b98f-59866831c2b2\.system_generated\steps\361\content.md"
OUTPUT_MD = "LISTA_SENHAS.md"

SECTOR_SIZE = 2352
HEADER_SIZE = 24
TABLE_OFFSET_IN_WA = 0xFB9800

def get_names_from_html():
    if not os.path.exists(HTML_PATH):
        return {}
    with open(HTML_PATH, "r", encoding="utf-8", errors="ignore") as f:
        html = f.read()
    
    # Try regex patterns to extract card id and name
    # Usually: <td>001</td>...title="Blue-Eyes White Dragon" or similar
    matches = re.findall(r'<td[^>]*>(\d{3})</td>\s*<td[^>]*><a[^>]+title="([^"]+)"', html)
    name_map = {}
    for cid, name in matches:
        clean_name = re.sub(r'\s*\((?:FMR|card)\)', '', name, flags=re.IGNORECASE).strip()
        name_map[int(cid)] = clean_name
    return name_map

def get_rom_data():
    wa_lba = 10102
    start_sector = TABLE_OFFSET_IN_WA // 2048
    offset_in_sector = TABLE_OFFSET_IN_WA % 2048
    sectors_needed = (offset_in_sector + 723 * 8 + 2047) // 2048

    buf = bytearray()
    with open(ROM_PATH, "rb") as f:
        for s in range(sectors_needed):
            f.seek((wa_lba + start_sector + s) * SECTOR_SIZE + HEADER_SIZE)
            buf.extend(f.read(2048))
    
    table_data = buf[offset_in_sector:offset_in_sector + 723 * 8]
    
    entries = {}
    for i in range(1, 723):
        chunk = table_data[i*8:(i+1)*8]
        cost = struct.unpack("<I", chunk[:4])[0]
        # passcode in BCD: reversed bytes
        passcode_bytes = chunk[4:8][::-1].hex().upper()
        if passcode_bytes in ("FEFFFFFF", "00000000"):
            passcode = "-------- (Sem senha)"
        else:
            passcode = passcode_bytes
        entries[i] = (passcode, cost)
    return entries

def main():
    names = get_names_from_html()
    rom_data = get_rom_data()
    print(f"Nomes encontrados no HTML: {len(names)}")
    print(f"Registros da ROM encontrados: {len(rom_data)}")

    lines = [
        "# Lista Oficial de Senhas (Passcodes) — Yu-Gi-Oh! Forbidden Memories",
        "",
        "Esta lista contém todas as **722 cartas do jogo**, com suas respectivas senhas oficiais de 8 dígitos extraídas diretamente da ROM do jogo, além dos custos originais em Star Chips.",
        "",
        "> **Dica:** Para usar uma senha, vá no menu principal em **Password** (ou **Senha**), digite o código de 8 dígitos e confirme com o botão **X**.",
        "",
        "| ID | Nome da Carta | Senha (8 Dígitos) | Custo Original |",
        "| :---: | :--- | :---: | :---: |"
    ]

    for cid in range(1, 723):
        name = names.get(cid, f"Carta #{cid:03d}")
        passcode, cost = rom_data.get(cid, ("--------", 0))
        cost_str = f"{cost:,}" if cost > 0 else "0"
        lines.append(f"| {cid:03d} | **{name}** | `{passcode}` | {cost_str} |")

    with open(OUTPUT_MD, "w", encoding="utf-8") as out_f:
        out_f.write("\n".join(lines) + "\n")

    print(f"Arquivo {OUTPUT_MD} gerado com sucesso!")

if __name__ == "__main__":
    main()
