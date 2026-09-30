import os
import struct

ROM_PATH = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (PT-BR).bin")
SECTOR_SIZE = 2352
HEADER_SIZE = 24

def read_wa_slice(offset, length):
    wa_lba = 10102
    start_sector = offset // 2048
    offset_in_sector = offset % 2048
    sectors_needed = (offset_in_sector + length + 2047) // 2048

    buf = bytearray()
    with open(ROM_PATH, "rb") as f:
        for s in range(sectors_needed):
            f.seek((wa_lba + start_sector + s) * SECTOR_SIZE + HEADER_SIZE)
            buf.extend(f.read(2048))
    
    return bytes(buf[offset_in_sector:offset_in_sector + length])

def inspect_around():
    # Passwords are at 0xFB9800 (size 5776 = 722 * 8)
    # 0xFB9800 + 5776 = 0xFBAE90
    print("Inspecionando blocos de dados antes e depois de 0xFB9800...")
    
    # Let's check 64KB before 0xFB9800: from 0xFA0000 to 0xFB9800
    pre_data = read_wa_slice(0xFA0000, 0x19800) # ~100KB
    
    # Check if 3000 / 2500 is in pre_data
    be_stat = struct.pack("<HH", 3000, 2500)
    pos = pre_data.find(be_stat)
    if pos != -1:
        print(f"[ACHOU!] 3000/2500 em 0x{0xFA0000 + pos:X}")
    else:
        print("3000/2500 uint16 não encontrado diretamente antes de 0xFB9800.")
        
    # Check after 0xFBAE90
    post_data = read_wa_slice(0xFBAE90, 0x20000)
    pos2 = post_data.find(be_stat)
    if pos2 != -1:
        print(f"[ACHOU!] 3000/2500 em 0x{0xFBAE90 + pos2:X}")

    # Let's check strings/text in pre_data or post_data
    # Look for printable strings > 4 chars
    import re
    text_matches = re.findall(b"[A-Za-z0-9\x80-\xff ]{5,30}", pre_data[:10000])
    print(f"Exemplos de texto encontrados antes da tabela: {text_matches[:5]}")

if __name__ == "__main__":
    inspect_around()
