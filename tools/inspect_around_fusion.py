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

def inspect_around_fusion():
    # 0xF8F802 is where non-zero bytes start
    data = read_wa_slice(0xF8F800, 2048)
    print("Bytes em 0xF8F800:")
    print(data[:128].hex())

    # Let's inspect the sequence of 16-bit values
    shorts = struct.unpack(f"<{len(data)//2}H", data)
    print("\nPrimeiros 40 valores (uint16) a partir de 0xF8F800:")
    for idx, s in enumerate(shorts[:40]):
        print(f"[{idx:02d}] 0x{s:04X} ({s})", end=" | " if (idx+1)%5 != 0 else "\n")

if __name__ == "__main__":
    inspect_around_fusion()
