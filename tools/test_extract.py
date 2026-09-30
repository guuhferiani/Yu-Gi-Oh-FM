import os
import struct

ROM_PATH = os.path.join("rom", "Yu-Gi-Oh! Forbidden Memories (PT-BR).bin")
SECTOR_SIZE = 2352
HEADER_SIZE = 24 # Mode 2 Form 1 user data starts at offset 24

def extract_file(rom_path, lba, size, out_path=None):
    sectors_needed = (size + 2047) // 2048
    extracted_data = bytearray()

    with open(rom_path, "rb") as f:
        for s in range(sectors_needed):
            f.seek((lba + s) * SECTOR_SIZE + HEADER_SIZE)
            chunk = f.read(2048)
            extracted_data.extend(chunk)

    extracted_data = bytes(extracted_data[:size])
    if out_path:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "wb") as out_f:
            out_f.write(extracted_data)
        print(f"Extraído com sucesso: {out_path} ({len(extracted_data)} bytes)")
    return extracted_data

if __name__ == "__main__":
    # Test reading SLUS header and WA_MRG header
    slus_data = extract_file(ROM_PATH, 25, 1902592)
    print(f"SLUS Header: {slus_data[:8]}") # Should be b'PS-X EXE'
    
    # Read first 2048 bytes of WA_MRG
    wa_mrg_header = extract_file(ROM_PATH, 10102, 2048)
    print(f"WA_MRG primeiros 64 bytes (hex): {wa_mrg_header[:64].hex()}")
