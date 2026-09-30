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

def find_first_nz():
    full_table = read_wa_slice(0xF8DAD8, 65536)
    for i, b in enumerate(full_table):
        if b != 0:
            print(f"Primeiro byte não-zero no offset 0xF8DAD8 + 0x{i:X} (0x{0xF8DAD8 + i:X})")
            print(f"Bytes: {full_table[i:i+64].hex()}")
            break

if __name__ == "__main__":
    find_first_nz()
