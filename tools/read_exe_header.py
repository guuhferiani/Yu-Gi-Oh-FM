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

def parse_exe_header():
    slus = extract_file(ROM_PATH, 25, 2048)
    magic = slus[:8]
    initial_pc = struct.unpack("<I", slus[0x10:0x14])[0]
    initial_gp = struct.unpack("<I", slus[0x14:0x18])[0]
    load_addr = struct.unpack("<I", slus[0x18:0x1C])[0]
    data_size = struct.unpack("<I", slus[0x1C:0x20])[0]

    print(f"Magic: {magic}")
    print(f"Initial PC: 0x{initial_pc:08X}")
    print(f"Initial GP: 0x{initial_gp:08X}")
    print(f"Load Address: 0x{load_addr:08X}")
    print(f"Data Size: {data_size} bytes (0x{data_size:X})")

if __name__ == "__main__":
    parse_exe_header()
