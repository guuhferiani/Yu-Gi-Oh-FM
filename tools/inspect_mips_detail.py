import os
import struct

ROM_BIN = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (Mod).bin")
SECTOR_SIZE = 2352
HEADER_SIZE = 24

def inspect_mips():
    slus_data = bytearray()
    with open(ROM_BIN, "rb") as f:
        for s in range(50):
            f.seek((25 + s) * SECTOR_SIZE + HEADER_SIZE)
            slus_data.extend(f.read(2048))
    
    print("Instruções MIPS em torno de 0xAFF8:")
    for i in range(-8, 16):
        pos = 0xAFF8 + (i * 4)
        word = struct.unpack("<I", slus_data[pos:pos+4])[0]
        # Check if -500 is nearby (0xFE0C)
        imm = word & 0xFFFF
        print(f"  Offset 0x{pos:X}: 0x{word:08X} (imm: {imm} / signed: {struct.unpack('<h', struct.pack('<H', imm))[0]})")

if __name__ == "__main__":
    inspect_mips()
