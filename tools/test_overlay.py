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

def test_ram_overlay():
    # Calculate candidate for Fusion Table (RAM 0x8017C2D8)
    cand_offset = 0xF8DAD8
    print(f"Testando offset 0x{cand_offset:X} em WA_MRG:")
    data = read_wa_slice(cand_offset, 256)
    print(f"Primeiros 128 bytes: {data[:128].hex()}")

    # Check non-zero bytes in 65536 bytes
    full_table = read_wa_slice(cand_offset, 65536)
    non_zero = sum(1 for b in full_table if b != 0)
    print(f"Bytes não-zero em 64KB no offset 0x{cand_offset:X}: {non_zero} de {len(full_table)}")

    # Let's also check surrounding offsets to find the start of non-zero structured data
    for check_off in range(0xF80000, 0xFBA000, 0x1000):
        sample = read_wa_slice(check_off, 1024)
        nz = sum(1 for b in sample if b != 0)
        if nz > 500:
            print(f"Bloco com muitos dados em 0x{check_off:X}: {nz}/1024 bytes não-zero")

if __name__ == "__main__":
    test_ram_overlay()
