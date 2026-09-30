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

def inspect_fusion_structure():
    data = read_wa_slice(0xF8DAD8, 1024)
    # Print where non-zero bytes start
    first_nz = next(i for i, b in enumerate(data) if b != 0)
    print(f"Primeiro byte não-zero em 0xF8DAD8 + 0x{first_nz:X} (offset absoluto 0x{0xF8DAD8 + first_nz:X})")
    
    sample = data[first_nz:first_nz + 128]
    print(f"Bytes iniciais: {sample.hex()}")
    
    # Check if they are 16-bit integers
    shorts = struct.unpack(f"<{len(sample)//2}H", sample)
    print(f"Valores inteiros (uint16): {shorts[:20]}")

if __name__ == "__main__":
    inspect_fusion_structure()
