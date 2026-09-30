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

def check_passwords():
    slus = extract_file(ROM_PATH, 25, 1902592)
    # Target offset around 0x198808
    target_offset = 0x198808
    print(f"Bytes no offset 0x{target_offset:X}:")
    chunk = slus[target_offset:target_offset + 64]
    print(chunk.hex())

    # Let's search for 999,999 (0x000F423F -> little endian 3F 42 0F 00)
    be_cost = struct.pack("<I", 999999)
    print(f"\nBuscando custo 999.999 ({be_cost.hex()}) no SLUS...")
    pos = 0
    matches = []
    while True:
        pos = slus.find(be_cost, pos)
        if pos == -1:
            break
        matches.append(pos)
        pos += 1
    print(f"Total de ocorrências de 999.999 encontradas: {len(matches)}")
    for m in matches[:10]:
        # print 16 bytes around
        surrounding = slus[m-4:m+12]
        print(f"Offset 0x{m:X}: {surrounding.hex()}")

if __name__ == "__main__":
    check_passwords()
