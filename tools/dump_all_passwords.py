import os
import struct

ROM_PATH = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (PT-BR).bin")
SECTOR_SIZE = 2352
HEADER_SIZE = 24
TABLE_OFFSET_IN_WA = 0xFB9800

def dump_722_passwords():
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
    
    entries = []
    for i in range(1, 723):
        chunk = table_data[i*8:(i+1)*8]
        cost, raw_pass = struct.unpack("<II", chunk)
        # Convert raw_pass (BCD) to string
        pass_hex = f"{raw_pass:08X}"
        passcode = "".join(reversed([pass_hex[j:j+2] for j in range(0, len(pass_hex), 2)]))
        entries.append((i, passcode, cost))
    
    return entries

if __name__ == "__main__":
    cards = dump_722_passwords()
    print(f"Total de cartas extraídas: {len(cards)}")
    for c in cards[:10]:
        print(f"Card #{c[0]:03d}: Senha: {c[1]} | Custo: {c[2]:,}")
    print("...")
    for c in cards[-5:]:
        print(f"Card #{c[0]:03d}: Senha: {c[1]} | Custo: {c[2]:,}")
