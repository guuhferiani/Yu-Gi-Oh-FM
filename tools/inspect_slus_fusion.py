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

def inspect_slus_fusion():
    slus = extract_file(ROM_PATH, 25, 1902592)
    # Check 0x16CAD8
    offset = 0x16CAD8
    print(f"SLUS offset 0x{offset:X} (RAM 0x8017C2D8):")
    chunk = slus[offset:offset+128]
    print(f"Hex: {chunk.hex()}")
    
    # Check if there is non-zero data
    non_zero = [i for i, b in enumerate(slus[offset:offset+65536]) if b != 0]
    print(f"Total de bytes não-zero em 64KB a partir de 0x{offset:X}: {len(non_zero)}")

if __name__ == "__main__":
    inspect_slus_fusion()
