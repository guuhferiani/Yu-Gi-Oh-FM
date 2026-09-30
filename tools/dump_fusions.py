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

def analyze_fusion_table():
    # In PS1 YGO FM:
    # RAM 8017C2D8 is the fusion table (65536 bytes).
    # In WA_MRG: offset 0xF8DAD8 to 0xF9DAD8 (64 KB).
    data = read_wa_slice(0xF8DAD8, 65536)
    
    # The first part of the fusion table is usually an offset/pointer table
    # There are 722 cards + types.
    # Let's inspect the first 722 * 2 = 1444 bytes (pointers)
    pointers = struct.unpack("<722H", data[:1444])
    print("Primeiros 10 ponteiros da tabela de fusão:")
    for i in range(10):
        ptr = pointers[i]
        print(f"Card #{i+1:03d} -> Ponteiro: 0x{ptr:04X} ({ptr})")

    # Let's inspect the data pointed to by Card #4 (Baby Dragon) or other cards
    for card_idx in [3, 15, 81]: # 0-indexed: Card 4, 16, 82
        ptr = pointers[card_idx]
        if ptr != 0:
            print(f"\nFusões da Carta #{card_idx+1:03d} (aponta para offset relativo 0x{ptr:04X}):")
            # Read bytes until 0x0000 or 0xFFFE
            chunk = data[ptr:ptr+64]
            # Each fusion entry is typically [material 2 (2 bytes)] [result (2 bytes)]
            entries = []
            for j in range(0, len(chunk), 4):
                val1, val2 = struct.unpack("<HH", chunk[j:j+4])
                if val1 == 0 or val1 == 0xFFFF or val1 == 0xFFFE:
                    break
                entries.append((val1, val2))
            for mat2, res in entries:
                print(f"   + Matéria 0x{mat2:04X} ({mat2}) -> Resultado: Carta #{res:03d}")

if __name__ == "__main__":
    analyze_fusion_table()
