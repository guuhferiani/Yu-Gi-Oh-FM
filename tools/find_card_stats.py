import os
import struct

ROM_PATH = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (PT-BR).bin")
SECTOR_SIZE = 2352
HEADER_SIZE = 24

def find_card_stats():
    # Blue-Eyes: 3000, 2500
    # Mystical Elf: 800, 2000
    # Hitotsu-Me Giant: 1200, 1000
    # Let's search in WA_MRG for 3000, 2500
    wa_lba = 10102
    wa_size = 37748736
    sectors = (wa_size + 2047) // 2048

    print("Buscando tabela de atributos de cartas (ATK/DEF)...")
    with open(ROM_PATH, "rb") as f:
        # We can read in 2MB chunks
        chunk_sectors = 1024
        for start_s in range(0, sectors, chunk_sectors):
            count = min(chunk_sectors, sectors - start_s)
            buf = bytearray()
            for s in range(count):
                f.seek((wa_lba + start_s + s) * SECTOR_SIZE + HEADER_SIZE)
                buf.extend(f.read(2048))
            
            # Check for 3000 (0x0BB8) as uint16
            be_atk = struct.pack("<H", 3000)
            be_def = struct.pack("<H", 2500)
            elf_atk = struct.pack("<H", 800)
            elf_def = struct.pack("<H", 2000)
            
            pos = 0
            while True:
                pos = buf.find(be_atk, pos)
                if pos == -1:
                    break
                # Check if DEF is nearby (e.g. at pos+2, pos+4, or pos-2)
                # Test various struct sizes: e.g. 10, 12, 16, 20 bytes
                for struct_size in [6, 8, 10, 12, 14, 16, 18, 20, 24, 32]:
                    # If this is card #1, card #2 should be struct_size away
                    # Check if elf_atk is at pos + struct_size or pos + struct_size - offset
                    # Let's check if buf[pos:pos+struct_size] contains be_def
                    if be_def in buf[pos-8:pos+16]:
                        # Check next card
                        c2 = buf[pos+struct_size-8:pos+struct_size+16]
                        if elf_atk in c2 and elf_def in c2:
                            abs_pos = start_s * 2048 + pos
                            print(f"\n[SUCESSO] Tabela de Cartas encontrada no offset de WA_MRG: 0x{abs_pos:X}")
                            print(f"Tamanho da estrutura por carta: {struct_size} bytes")
                            return abs_pos, struct_size
                pos += 1

if __name__ == "__main__":
    find_card_stats()
