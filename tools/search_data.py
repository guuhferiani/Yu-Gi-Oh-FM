import os
import struct

ROM_PATH = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (PT-BR).bin")
SECTOR_SIZE = 2352
HEADER_SIZE = 24

def extract_file(rom_path, lba, size):
    sectors_needed = (size + 2047) // 2048
    extracted_data = bytearray()
    with open(rom_path, "rb") as f:
        for s in range(sectors_needed):
            f.seek((lba + s) * SECTOR_SIZE + HEADER_SIZE)
            chunk = f.read(2048)
            extracted_data.extend(chunk)
    return bytes(extracted_data[:size])

def search_patterns():
    # Extract SLUS
    print("Extraindo SLUS_014.11...")
    slus = extract_file(ROM_PATH, 25, 1902592)
    
    # Blue-Eyes ATK: 3000 (0x0BB8), DEF: 2500 (0x09C4)
    be_stat = struct.pack("<HH", 3000, 2500)
    print(f"Buscando padrão ATK 3000 / DEF 2500 ({be_stat.hex()})...")
    
    pos = 0
    while True:
        pos = slus.find(be_stat, pos)
        if pos == -1:
            break
        print(f"Encontrado em SLUS no offset 0x{pos:X}")
        pos += 1

    # Also search in the first few MB of WA_MRG
    print("\nExtraindo primeiros 4MB de WA_MRG.MRG...")
    wa_sample = extract_file(ROM_PATH, 10102, 4 * 1024 * 1024)
    pos = 0
    while True:
        pos = wa_sample.find(be_stat, pos)
        if pos == -1:
            break
        print(f"Encontrado em WA_MRG no offset 0x{pos:X}")
        pos += 1

    # Search for card text/name in SLUS or WA_MRG
    for name in [b"Blue-Eyes", b"Dragao", b"Drag\xe3o", b"Mago Negro", b"Dark Magician", b"SIMON"]:
        found_slus = slus.find(name)
        if found_slus != -1:
            print(f"Texto '{name.decode('latin-1')}' encontrado no SLUS em 0x{found_slus:X}")
        found_wa = wa_sample.find(name)
        if found_wa != -1:
            print(f"Texto '{name.decode('latin-1')}' encontrado no WA_MRG em 0x{found_wa:X}")

if __name__ == "__main__":
    search_patterns()
