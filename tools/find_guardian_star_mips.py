import os
import struct

EXE_PATH = os.path.join("pc_game", "yfm-redecomp-v0.1.2", "memories-pc.exe")
ROM_BIN = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (Mod).bin")

SECTOR_SIZE = 2352
HEADER_SIZE = 24

def check_ps1_slus():
    # Read SLUS_014.11 from LBA 25
    lba = 25
    size = 1902592
    sectors = (size + 2047) // 2048
    slus_data = bytearray()
    with open(ROM_BIN, "rb") as f:
        for s in range(sectors):
            f.seek((lba + s) * SECTOR_SIZE + HEADER_SIZE)
            slus_data.extend(f.read(2048))
    slus = bytes(slus_data[:size])

    # Search for addiu reg, zero, 500 (0x240X01F4) -> little endian: F4 01 X 24
    print("Buscando instruções MIPS com 500 (0x01F4) no SLUS do PS1...")
    matches = []
    for pos in range(0, len(slus)-4, 4):
        word = struct.unpack("<I", slus[pos:pos+4])[0]
        # Check if lowest 16 bits is 500 (0x01F4) and opcode is addiu (0x24000000) or ori (0x34000000)
        imm = word & 0xFFFF
        opcode = (word >> 26) & 0x3F
        if imm == 0x01F4 and opcode in (0x09, 0x0D): # addiu or ori
            matches.append((pos, word))

    print(f"Total de ocorrências MIPS com 500 no SLUS: {len(matches)}")
    for pos, word in matches:
        print(f"  Offset 0x{pos:X} (RAM 0x{0x80010000 - 0x800 + pos:08X}): 0x{word:08X}")

if __name__ == "__main__":
    check_ps1_slus()
