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

def inspect_table():
    # Card #1 Blue-Eyes: Password 89631139, Cost 999999
    # Check around 0xFB9800
    data = read_wa_slice(0xFB9800, 64)
    print("Dados em 0xFB9800 (16 cards x 8 bytes):")
    for i in range(8):
        entry = data[i*8:(i+1)*8]
        val1, val2 = struct.unpack("<II", entry)
        print(f"Card #{i+1:03d}: {entry.hex()} | Val1: {val1} (0x{val1:08X}) | Val2: {val2} (0x{val2:08X})")

if __name__ == "__main__":
    inspect_table()
