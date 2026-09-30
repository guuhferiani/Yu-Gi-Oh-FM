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

# Check drop tables in WA_MRG
# In YGO FM, the drop tables are located around 0xF80000 - 0xF8F000
def scan_card_in_drops(target_cards):
    print("Analisando presença das cartas nas tabelas de drop do jogo original...")
    # Read the drop area (around 120KB)
    drop_data = read_wa_slice(0xF80000, 0x10000)
    
    for card_id, name in target_cards:
        # Card IDs are stored as 2-byte integers (uint16)
        needle = struct.pack("<H", card_id)
        count = drop_data.count(needle)
        print(f"Card #{card_id:03d} - {name}: aparece {count} vezes nas tabelas brutas da ROM.")

if __name__ == "__main__":
    CARDS = [
        (1, "Dragão Branco de Olhos Azuis"),
        (4, "Dragão Bebê"),
        (35, "Mago Negro"),
        (82, "Dragão Negro de Olhos Vermelhos"),
        (336, "Raigeki"),
        (657, "Megamorfo"),
    ]
    scan_card_in_drops(CARDS)
