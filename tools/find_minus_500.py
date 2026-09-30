import os
import struct

ROM_BIN = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (Mod).bin")
SECTOR_SIZE = 2352
HEADER_SIZE = 24

def find_slus_func():
    # Read SLUS_014.11
    lba = 25
    size = 1902592
    sectors = (size + 2047) // 2048
    slus_data = bytearray()
    with open(ROM_BIN, "rb") as f:
        for s in range(sectors):
            f.seek((lba + s) * SECTOR_SIZE + HEADER_SIZE)
            slus_data.extend(f.read(2048))
    slus = bytes(slus_data[:size])

    # Search for -500 (0xFE0C) in SLUS
    print("Buscando instruções com -500 (0xFE0C) no SLUS...")
    for pos in range(0, len(slus)-4, 4):
        word = struct.unpack("<I", slus[pos:pos+4])[0]
        if (word & 0xFFFF) == 0xFE0C:
            print(f"  Offset 0x{pos:X}: 0x{word:08X}")
            # print surrounding 10 instructions
            for j in range(-5, 6):
                w = struct.unpack("<I", slus[pos+j*4:pos+(j+1)*4])[0]
                print(f"    [0x{pos+j*4:X}] 0x{w:08X}")

if __name__ == "__main__":
    find_slus_func()
